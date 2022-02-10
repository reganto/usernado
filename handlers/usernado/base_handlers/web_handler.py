import hashlib
import secrets
import tornado.web
from tornado.escape import xhtml_escape


class BaseValidationError(ValueError):
    pass


class UserDoesNotExistError(BaseValidationError):
    pass


class UserAlreadyExistError(BaseValidationError):
    pass


class UnsupportedUserModelError(BaseValidationError):
    pass


class AuthStrategy:
    _salt = secrets.token_hex()

    @classmethod
    def hash_password(cls, password: str, salt: bytes = _salt) -> str:
        password = password.encode('utf-8')
        hashed_password = hashlib.sha512(password + salt.encode()).hexdigest()
        return hashed_password

    @classmethod
    def _sqlalchemy_register(cls, klass, user_model, username, password):
        NotImplemented

    @classmethod
    def _sqlalchemy_login(cls, klass, user_model, username, password):
        NotImplemented

    @classmethod
    def _peewee_register(cls, klass, user_model, username, password):
        hashed_password = cls.hash_password(password)
        user_already_exist = user_model.select().where(
            user_model.username == username).first()
        if user_already_exist:
            raise UserAlreadyExistError(user_already_exist)
        else:
            user_model.create(
                username=username,
                password=hashed_password,
                salt=cls._salt
            )
            klass.set_secure_cookie("username", klass.get_argument("username"))

    @classmethod
    def _peewee_login(cls, klass, user_model, username, password):
        user_exist = user_model.select().where(user_model.username == username).first()
        if not user_exist:
            raise UserDoesNotExistError("User does not exist")
        hashed_password = cls.hash_password(password, salt=user_exist.salt)

        if user_exist and user_exist.password == hashed_password:
            klass.set_secure_cookie("username", username)
        else:
            raise PermissionError("You'r username or password is incorrent")


class WebHandler(tornado.web.RequestHandler):
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
                AuthStrategy._peewee_register(
                    klass=self,
                    user_model=user_model,
                    username=username,
                    password=password,
                )
            else:
                raise UnsupportedUserModelError(user_model)
        except ModuleNotFoundError:
            try:
                import sqlalchemy
                if isinstance(user_model, sqlalchemy.Model):
                    AuthStrategy._sqlalchemy_register(
                        klass=self,
                        user_model=user_model,
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
                AuthStrategy._peewee_login(
                    klass=self,
                    user_model=user_model,
                    username=username,
                    password=password,
                )
            else:
                raise UnsupportedUserModelError(user_model)
        except ModuleNotFoundError:
            try:
                import sqlalchemy
                if isinstance(user_model, sqlalchemy.Model):
                    AuthStrategy._sqlalchemy_login(
                        klass=self,
                        user_model=user_model,
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
        """Get argument from client then scaped it

        :param argument: incoming argument
        :type argument: str
        :return: scaped argument
        :rtype: str
        """
        return self.get_argument(xhtml_escape(argument))
