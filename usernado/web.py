"""If you want to add support for other ORM:

1. Create a class which implement :class:`IAuth` interface with name convention like  ``_OrmNameAuth``.

2. Override :class:`~IAuth.register` and :class:`~IAuth.login` methods

3. Add model check logic in :class:`WebHandler`'s :class:`~WebHandler.register` and :class:`~WebHandler.login` methods.
"""

from abc import ABCMeta, abstractmethod
import hashlib
import secrets
from typing import Optional, Union, Any

import sqlalchemy
import peewee
import tornado
from tornado.escape import xhtml_escape

from .base import BaseHandler


class UserDoesNotExistError(ValueError):
    pass


class UserAlreadyExistError(ValueError):
    pass


class PermissionDeniedError(ValueError):
    pass


class UnsupportedUserModelError(ValueError):
    pass


_SALT = secrets.token_hex()


def _hash_password(password: str, salt: str = _SALT) -> str:
    """Generate hashed password.

    :param password: Incoming password.
    :type password: str
    :param salt: A salt to make hashing more strength, defaults to _SALT
    :type salt: str, optional
    :return: A hashed password.
    :rtype: str
    """

    password = password.encode("utf-8")
    hashed_password = hashlib.sha512(password + salt.encode()).hexdigest()
    return hashed_password


def _sqlalchemy_session_maker() -> "sqlalchemy.orm.sessionmaker":
    """Generate a session for SQLAlchemy.

    .. note:: I'm not sure this is a good implementiation for
    generating sqlalchemy sessions.

    :return: A generated sqlalchemy session
    :rtype: sqlalchemy.orm.sessionmaker
    """

    import database
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(database.models.DB)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


class IAuth(metaclass=ABCMeta):
    """Every ORM specific authentication class MUST implement
    this Interface and override ``register`` and ``login`` mehtods.
    """

    @staticmethod
    @abstractmethod
    def register(
        request: tornado.httpclient.HTTPRequest,
        model: Union[peewee.Model, "sqlalchemy.orm.declarative_base"],
        username: str,
        password: str,
    ) -> bool:
        """Abstract register method.

        :param request: Incoming HTTP request.
        :type request: tornado.httpclient.HTTPRequest
        :param model: ORM model.
        :type model: Union[peewee.Model, sqlalchemy.orm.declarative_base]
        :param username: Username.
        :type username: str
        :param password: Password.
        :type password: str
        :return: True if user registration done successfully otherwise False.
        :rtype: bool
        """
        NotImplementedError

    @staticmethod
    @abstractmethod
    def login(
        request: tornado.httpclient.HTTPRequest,
        model: Union[peewee.Model, "sqlalchemy.orm.declarative_base"],
        username: str,
        password: str,
    ) -> bool:
        """Abstract login method.

        :param request: Incoming HTTP request.
        :type request: tornado.httpclient.HTTPRequest
        :param model: ORM model.
        :type model: Union[peewee.Model, sqlalchemy.orm.declarative_base]
        :param username: Username.
        :type username: str
        :param password: Password.
        :type password: str
        :return: True if user registration done successfully otherwise False.
        :rtype: bool
        """
        NotImplementedError


class _PeeweeAuth(IAuth):
    """Peewee specific authentication class."""

    @staticmethod
    def register(
        request: tornado.httpclient.HTTPRequest,
        model: Union[peewee.Model, "sqlalchemy.orm.declarative_base"],
        username: str,
        password: str,
    ) -> bool:
        hashed_password = _hash_password(password)
        user_already_exist = model.filter(model.username == username).first()

        if user_already_exist:
            raise UserAlreadyExistError

        try:
            model.create(
                username=username,
                password=hashed_password,
                salt=_SALT,
            )
        except Exception as e:
            print("Error in user registration proccess: ", e)
        else:
            return True

    @staticmethod
    def login(
        request: tornado.httpclient.HTTPRequest,
        model: Union[peewee.Model, "sqlalchemy.orm.declarative_base"],
        username: str,
        password: str,
    ) -> bool:
        try:
            user = model.filter(model.username == username).first()
        except Exception:
            raise UserDoesNotExistError
        else:
            hashed_password = _hash_password(password, salt=user.salt)

        if user and user.password == hashed_password:
            request.set_secure_cookie(
                "username",
                username,
                secure=True,
                httpOnly=True,
            )
            return True
        else:
            raise PermissionDeniedError("Your username or password is NOT correct.")


class _SQLAlchemy(IAuth):
    """SQLAlchemy specific authentication class."""

    @staticmethod
    def register(
        request: tornado.httpclient.HTTPRequest,
        model: Union[peewee.Model, "sqlalchemy.orm.declarative_base"],
        username: str,
        password: str,
    ) -> bool:
        hashed_password = _hash_password(password)
        session = _sqlalchemy_session_maker()
        user_already_exist = session.query(model).filter_by(username=username).first()

        if user_already_exist:
            raise UserAlreadyExistError(user_already_exist)

        try:
            user = model(username=username, password=hashed_password, salt=_SALT)
            session.add(user)
            session.commit()
        except Exception as e:
            print("Error in user registration proccess: ", e)
            session.rollback()
        else:
            return True
        finally:
            session.close()

    @staticmethod
    def login(
        request: tornado.httpclient.HTTPRequest,
        model: Union[peewee.Model, "sqlalchemy.orm.declarative_base"],
        username: str,
        password: str,
    ) -> bool:
        session = _sqlalchemy_session_maker()
        user_exist = session.query(model).filter_by(username=username).first()

        if not user_exist:
            raise UserDoesNotExistError("User does not exist.")

        hashed_password = _hash_password(password, salt=user_exist.salt)

        if user_exist and user_exist.password == hashed_password:
            request.set_secure_cookie(
                "username",
                username,
                secure=True,
                httpOnly=True,
            )
            return True
        else:
            raise PermissionDeniedError("Your username or password is NOT correct.")


class WebHandler(BaseHandler):
    """Every HTTP request handler MUST inherit from ``WebHandler``."""

    def register(
        self,
        model: Union[peewee.Model, "sqlalchemy.orm.declarative_base"],
        username: str,
        password: str,
    ) -> bool:
        """Signup user with provided username and password.

        :param model: ORM model.
        :type model: Union[peewee.Model, sqlalchemy.orm.declarative_base]
        :param username: Username.
        :type username: str
        :param password: Password.
        :type password: str
        :raises UnsupportedUserModelError: Raised when auth operation for ``model`` was not provided.
        :return: True if user registration done successfully otherwise False.
        :rtype: bool
        """

        try:
            import peewee

            if issubclass(model, peewee.Model):
                return _PeeweeAuth.register(
                    request=self,
                    model=model,
                    username=username,
                    password=password,
                )
            else:
                raise UnsupportedUserModelError
        except (ModuleNotFoundError, UnsupportedUserModelError):
            try:
                import sqlalchemy

                if model.metadata:
                    # I've no experience in sqlalchemy so I look for a better
                    # implementation to check if model is type of sqlalchemy or not.
                    return _SQLAlchemy.register(
                        request=self,
                        model=model,
                        username=username,
                        password=password,
                    )
                else:
                    raise UnsupportedUserModelError
            except ModuleNotFoundError:
                self.write("<h3>Install <b>SQLAlchemy</b> or <b>Peewee</b> first.</h3>")

    def login(
        self,
        model: Union[peewee.Model, "sqlalchemy.orm.declarative_base"],
        username: str,
        password: str,
    ) -> bool:
        """Signin user with provided username and password.

        :param model: ORM model.
        :type model: Union[peewee.Model, sqlalchemy.orm.declarative_base]
        :param username: Username.
        :type username: str
        :param password: Password.
        :type password: str
        :raises UnsupportedUserModelError: Raised when auth operation for ``model`` was not provided.
        :return: True if user login done successfully otherwise False.
        :rtype: bool
        """

        try:
            import peewee

            if issubclass(model, peewee.Model):
                return _PeeweeAuth.login(
                    request=self,
                    model=model,
                    username=username,
                    password=password,
                )
            else:
                raise UnsupportedUserModelError(model)
        except (ModuleNotFoundError, UnsupportedUserModelError):
            try:
                import sqlalchemy

                if model.metadata:
                    # I've no experience in sqlalchemy so I look for a better
                    # implementation to check if model is type of sqlalchemy or not.
                    return _SQLAlchemy.login(
                        request=self,
                        model=model,
                        username=username,
                        password=password,
                    )
                else:
                    raise UnsupportedUserModelError
            except ModuleNotFoundError:
                self.write("<h3>Install <b>SQLAlchemy</b> or <b>Peewee</b> first.</h3>")

    def logout(self) -> None:
        """Logout user."""

        self.clear_cookie("username")

    @property
    def authenticate(self) -> bool:
        """Check if current user is authenticated?

        :rtype: bool
        """

        return bool(self.current_user)

    def get_current_user(self) -> Optional[bytes]:
        """To implement user authentication we need to override this method.

        for more information, take a look at `Tornado documentation <https://www.tornadoweb.org/en/stable/guide/security.html?highlight=get_current_user#user-authentication>`_.

        :return: A secure cookie.
        :rtype: Optional[bytes]
        """

        return self.get_secure_cookie("username")

    def redirect_to_route(self, name: str, *args: Any) -> None:
        """Redirect to particular route.

        :param name: Named route
        :type name: str
        """

        self.redirect(self.reverse_url(name, *args))

    def get_escaped_argument(
        self,
        name: str,
        default: Optional[str] = None,
        strip: bool = True,
    ) -> str:
        """Returns the xhtml escaped value of the argument with the given name.

        :param name: Name of the desired argument.
        :type name: str
        :param default: Default value for non existing argument, defaults to None.
        :type default: Optional[str], optional
        :param strip: Strip argument value, defaults to True.
        :type strip: bool, optional
        :return: Escaped argument.
        :rtype: str
        """
        argument = self.get_argument(name, default, strip)
        return xhtml_escape(argument)
