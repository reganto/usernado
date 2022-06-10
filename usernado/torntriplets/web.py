"""If you want to add support for other ORM's:
01- Create a class which implement `IAuth` interface
 with name convention like so: ORMNAMEAuth
02- Override `register` and `login` methods
03- Add model check logic in WebHandler's register
 and login methods.
"""

import hashlib
import secrets
from abc import ABCMeta, abstractmethod
from typing import Optional, Union

from tornado.escape import xhtml_escape

from usernado.torntriplets.base import BaseHandler


class BaseValidationError(ValueError):
    pass


class UserDoesNotExistError(BaseValidationError):
    pass


class UserAlreadyExistError(BaseValidationError):
    pass


class PermissionDeniedError(BaseValidationError):
    pass


class UnsupportedUserModelError(BaseValidationError):
    pass


_SALT = secrets.token_hex()


def _hash_password(password: str, salt: str = _SALT) -> str:
    """Generate hashed password.

    :param password: Incomming password
    :type password: str
    :param salt: A salt to make hashing more strength, defaults to _SALT
    :type salt: str, optional
    :return: A hashed password
    :rtype: str
    """

    password = password.encode("utf-8")
    hashed_password = hashlib.sha512(password + salt.encode()).hexdigest()
    return hashed_password


def _sqlalchemy_session_maker():
    """Generate a session for SQLAlchemy.

    There seems to be a better implementation to do this!"""

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    import database

    engine = create_engine(database.models.DB)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


class IAuth(metaclass=ABCMeta):
    """Every ORM specific authentication class MUST implement
    this Interface and override `register` and `login` mehtods.
    """

    @staticmethod
    @abstractmethod
    def register(request, model, username, password):
        NotImplementedError

    @staticmethod
    @abstractmethod
    def login(request, model, username, password):
        NotImplementedError


class PeeweeAuth(IAuth):
    """Peewee specific authentication class."""

    def register(request, model, username, password):
        hashed_password = _hash_password(password)
        user_already_exist = model.select().where(model.username == username).first()

        if user_already_exist:
            raise UserAlreadyExistError(user_already_exist)

        try:
            model.create(username=username, password=hashed_password, salt=_SALT)
        except Exception as e:
            print("Error in user registration proccess: ", e)
        else:
            return True

    def login(request, model, username, password):
        user = None
        try:
            user = model.filter(model.username == username).first()
        except Exception:
            raise UserDoesNotExistError
        else:
            hashed_password = _hash_password(password, salt=user.salt)

        if user and user.password == hashed_password:
            request.set_secure_cookie("username", username)
            return True
        else:
            raise PermissionDeniedError("Your username or password is NOT correct.")


class SQLAlchemy(IAuth):
    """SQLAlchemy specific authentication class."""

    def register(request, model, username, password):
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

    def login(request, model, username, password):
        session = _sqlalchemy_session_maker()
        user_exist = session.query(model).filter_by(username=username).first()

        if not user_exist:
            raise UserDoesNotExistError("User does not exist.")

        hashed_password = _hash_password(password, salt=user_exist.salt)

        if user_exist and user_exist.password == hashed_password:
            request.set_secure_cookie("username", username)
            return True
        else:
            raise PermissionDeniedError("Your username or password is NOT correct.")


class WebHandler(BaseHandler):
    def register(self, user_model, username: str, password: str) -> bool:
        """Signup user with provided username and password.

        :param user_model: User model
        :type user_model: SQLAlchemy | Peewee |
        :param username: Username
        :type username: str
        :param password: Password
        :type password: str
        :raises UnsupportedUserModelError: If user_model was not
          an instance of SQLAlchemy or Peewee.
        :return: Return True, If user registration is successful.
        :rtype: bool
        """

        try:
            import peewee

            if issubclass(user_model, peewee.Model):
                return PeeweeAuth.register(
                    request=self,
                    model=user_model,
                    username=username,
                    password=password,
                )
            else:
                raise UnsupportedUserModelError(user_model)
        except (ModuleNotFoundError, UnsupportedUserModelError):
            try:
                import sqlalchemy

                if user_model.metadata:
                    # I've no experience in sqlalchemy so I look for a better
                    # implementation to check if user_model is type of sqlalchemy or not.
                    return SQLAlchemy.register(
                        request=self,
                        model=user_model,
                        username=username,
                        password=password,
                    )
                else:
                    raise UnsupportedUserModelError(user_model)
            except ModuleNotFoundError:
                self.write("<h3>You have to install SQLAlchemy or Peewee first.</h3>")

    def login(self, user_model, username: str, password: str) -> bool:
        """Signin user with provided username and password.

        :param user_model: User model
        :type user_model: SQLAlchemy | Peewee |
        :param username: Username
        :type username: str
        :param password: Password
        :type password: str
        :raises UnsupportedUserModelError: If user_model was not
          an instance of SQLAlchemy or Peewee.
        :return: Return True, if user login is successful.
        :rtype: True
        """

        try:
            import peewee

            if issubclass(user_model, peewee.Model):
                return PeeweeAuth.login(
                    request=self,
                    model=user_model,
                    username=username,
                    password=password,
                )
            else:
                raise UnsupportedUserModelError(user_model)
        except (ModuleNotFoundError, UnsupportedUserModelError):
            try:
                import sqlalchemy

                if user_model.metadata:
                    # I've no experience in sqlalchemy so I look for a better
                    # implementation to check if user_model is type of sqlalchemy or not.
                    return SQLAlchemy.login(
                        request=self,
                        model=user_model,
                        username=username,
                        password=password,
                    )
                else:
                    raise UnsupportedUserModelError(user_model)
            except ModuleNotFoundError:
                self.write("<h3>You have to install SQLAlchemy or Peewee first.</h3>")

    def logout(self) -> None:
        """Logout user."""

        self.clear_cookie("username")

    @property
    def authenticate(self) -> bool:
        """Check if current user is authenticated.

        :rtype: bool
        """

        return bool(self.current_user)

    def get_current_user(self) -> str:
        """To implement user authentication we need to override this method.

        for more information, take a look at Tornado documentation.
        https://www.tornadoweb.org/en/stable/guide/security.html?highlight=get_current_user#user-authentication

        :return: A secure cookie
        :rtype: str
        """

        return self.get_secure_cookie("username")

    def redirect_to_route(self, name: str):
        """Redirect to particular route.

        :param name: Named route
        :type name: str
        """

        self.redirect(self.reverse_url(name))

    def get_escaped_argument(
        self,
        name: str,
        default: Union[None, str],
        strip: bool = True,
    ) -> Optional[str]:
        """Returns the escaped value of the argument with the given name.

        :param name: Name of desired argument
        :type name: str
        :return: Escaped argument
        :rtype: str
        """
        argument = self.get_argument(name, default, strip)
        return xhtml_escape(argument)
