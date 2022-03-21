import hashlib
import secrets
from abc import ABCMeta, abstractmethod
from typing import Optional

from tornado.escape import xhtml_escape
from usernado.torntriplets.base import BaseHandler


class BaseValidationError(ValueError):
    pass


class UserDoesNotExistError(BaseValidationError):
    pass


class UserAlreadyExistError(BaseValidationError):
    pass


class UnsupportedUserModelError(BaseValidationError):
    pass


SALT = secrets.token_hex()


def _hash_password(password: str, salt: Optional[hex] = SALT) -> str:
    """_summary_ TODO

    :param password: _description_
    :type password: str
    :param salt: _description_, defaults to SALT
    :type salt: Optional[hex], optional
    :return: _description_
    :rtype: str
    """
    password = password.encode('utf-8')
    hashed_password = hashlib.sha512(password + salt.encode()).hexdigest()
    return hashed_password


# Is there better implementation to do this?
def _sqlalchemy_session_maker():
    """_summary_ TODO

    :return: _description_
    :rtype: _type_
    """
    import database
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    engine = create_engine(database.models.DB)
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


class IAuth(metaclass=ABCMeta):
    """_summary_ TODO

    :param metaclass: _description_, defaults to ABCMeta
    :type metaclass: _type_, optional
    """
    @staticmethod
    @abstractmethod
    def register(request, model, username, password):
        """_summary_ TODO

        :param request: _description_
        :type request: _type_
        :param model: _description_
        :type model: _type_
        :param username: _description_
        :type username: _type_
        :param password: _description_
        :type password: _type_
        """
        NotImplementedError

    @staticmethod
    @abstractmethod
    def login(request, model, username, password):
        """_summary_ TODO

        :param request: _description_
        :type request: _type_
        :param model: _description_
        :type model: _type_
        :param username: _description_
        :type username: _type_
        :param password: _description_
        :type password: _type_
        """
        NotImplementedError


class PeeweeAuth(IAuth):
    def register(request, model, username, password):
        """_summary_

        :param request: _description_
        :type request: _type_
        :param model: _description_
        :type model: _type_
        :param username: _description_
        :type username: _type_
        :param password: _description_
        :type password: _type_
        :raises UserAlreadyExistError: _description_
        :return: _description_
        :rtype: _type_
        """
        hashed_password = _hash_password(password)
        user_already_exist = model.select().where(
            model.username == username).first()
        if user_already_exist:
            raise UserAlreadyExistError(user_already_exist)
        try:
            model.create(
                username=username,
                password=hashed_password,
                salt=SALT
            )
        except Exception as e:
            print('Error in user registration proccess: ', e)
        else:
            return True

    def login(request, model, username, password):
        """_summary_

        :param request: _description_
        :type request: _type_
        :param model: _description_
        :type model: _type_
        :param username: _description_
        :type username: _type_
        :param password: _description_
        :type password: _type_
        :raises UserDoesNotExistError: _description_
        :raises PermissionError: _description_
        """
        user_exist = model.select().where(model.username == username).first()
        if not user_exist:
            raise UserDoesNotExistError("User does not exist")
        hashed_password = _hash_password(password, salt=user_exist.salt)

        if user_exist and user_exist.password == hashed_password:
            request.set_secure_cookie("username", username)
        else:
            raise PermissionError("You'r username or password is incorrent")


class SqlAclchemyAuth(IAuth):
    def register(request, model, username, password):
        """_summary_

        :param request: _description_
        :type request: _type_
        :param model: _description_
        :type model: _type_
        :param username: _description_
        :type username: _type_
        :param password: _description_
        :type password: _type_
        :raises UserAlreadyExistError: _description_
        :return: _description_
        :rtype: _type_
        """
        hashed_password = _hash_password(password)
        session = _sqlalchemy_session_maker()
        user_already_exist = session.query(
            model).filter_by(username=username).first()
        if user_already_exist:
            raise UserAlreadyExistError(user_already_exist)
        try:
            user = model(
                username=username,
                password=hashed_password,
                salt=SALT
            )
            session.add(user)
            session.commit()
        except Exception as e:
            print('Error in user registration proccess: ', e)
            session.rollback()
        else:
            return True
        finally:
            session.close()

    def login(request, model, username, password):
        """_summary_

        :param request: _description_
        :type request: _type_
        :param model: _description_
        :type model: _type_
        :param username: _description_
        :type username: _type_
        :param password: _description_
        :type password: _type_
        :raises UserDoesNotExistError: _description_
        :raises PermissionError: _description_
        """
        session = _sqlalchemy_session_maker()
        user_exist = session.query(model).filter_by(
            username=username).first()
        if not user_exist:
            raise UserDoesNotExistError("User does not exist")
        hashed_password = _hash_password(password, salt=user_exist.salt)

        if user_exist and user_exist.password == hashed_password:
            request.set_secure_cookie("username", username)
        else:
            raise PermissionError("You'r username or password is incorrent")


class WebHandler(BaseHandler):
    def register(self, user_model, username: str, password: str) -> None:
        """Register user with provided username and password

        :param user_model: user active record
        :type user_model: sqlalchemy.Model or peewee.Model
        :param username: username that provided by user
        :type username: str
        :param password: password that provided by user
        :type password: str
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
                if user_model.metadata:  # Is there a better implementation to do this?
                    return SqlAclchemyAuth.register(
                        request=self,
                        model=user_model,
                        username=username,
                        password=password,
                    )
                else:
                    raise UnsupportedUserModelError(user_model)
            except ModuleNotFoundError:
                self.write('<h3>You should install Peewee or SqlAlchemy.</h3>')

    def login(self, user_model, username: str, password: str) -> None:
        """Login user with provided username and password

        :param username: username that provided by user
        :type username: str
        :param password: password that provided by user
        :type password: str
        """

        try:
            import peewee
            if issubclass(user_model, peewee.Model):
                PeeweeAuth.login(
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
                if user_model.metadata:  # Is there a better implementation to do this?
                    SqlAclchemyAuth.login(
                        request=self,
                        model=user_model,
                        username=username,
                        password=password,
                    )
                else:
                    raise UnsupportedUserModelError(user_model)
            except ModuleNotFoundError:
                self.write('<h3>You should install Peewee or SqlAlchemy.</h3>')

    def logout(self) -> None:
        """Logout user"""
        self.clear_cookie("username")

    def authenticate(self) -> bool:
        """Current user is authenticated or not

        :rtype: bool
        """
        return bool(self.current_user)

    def get_current_user(self) -> str:
        """We should override this for auth process

        Look at docs for more information.

        :return: a secure cookie value
        :rtype: str
        """
        return self.get_secure_cookie('username')

    def redirect_to_route(self, name: str):
        """Redirect to specific route

        :param name: name of route
        :type name: str
        """

        self.redirect(self.reverse_url(name))

    def get_escaped_argument(self, argument) -> str:
        """Get argument from client then escaped it

        :param argument: incoming argument
        :type argument: str
        :return: scaped argument
        :rtype: str
        """
        return self.get_argument(xhtml_escape(argument))
