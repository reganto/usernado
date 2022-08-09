from pathlib import Path
import secrets

import peewee
from tornado.ioloop import IOLoop
from tornado.web import Application, authenticated, url

from usernado import WebHandler

BASE_DIR = Path(__file__).resolve().parent

# You can use either Peewee or Sqlalchemy as ORM
DB = peewee.SqliteDatabase("db.sqlite3")


class User(peewee.Model):
    """You have to provide these three fields at least."""

    username = peewee.CharField(max_length=100)
    password = peewee.CharField(max_length=100)
    salt = peewee.CharField(max_length=100)

    class Meta:
        database = DB

    def __str__(self):
        return self.username


DB.create_tables(
    [
        User,
    ],
    safe=True,
)


class RegisterHandler(WebHandler):
    def get(self):
        self.render("register.html")

    def post(self):
        username = self.get_escaped_argument("username", None)
        password = self.get_escaped_argument("password", None)
        try:
            self.register(User, username, password)
        except Exception as e:
            print(e)
        else:
            self.redirect_to_route("login")

    def check_xsrf_cookie(self) -> None:
        """Test purpose."""
        pass


class LoginHandler(WebHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        username = self.get_escaped_argument("username", None)
        password = self.get_escaped_argument("password", None)
        try:
            self.login(User, username, password)
        except Exception as e:
            print(e)
        else:
            self.redirect_to_route("dashboard")

    def check_xsrf_cookie(self) -> None:
        """Test purpose."""
        pass


class LogoutHandler(WebHandler):
    def get(self):
        if self.authenticate():
            self.logout()
        self.redirect_to_route("login")


class DashboardHandler(WebHandler):
    @authenticated
    def get(self):
        self.write("Dashborad")


class App(Application):
    def __init__(self):
        handlers = [
            url("/", DashboardHandler, name="dashboard"),
            url("/auth/register/", RegisterHandler, name="register"),
            url("/auth/login/", LoginHandler, name="login"),
            url("/auth/logout/", LogoutHandler, name="logout"),
        ]
        settings = dict(
            debug=True,
            cookie_secret=secrets.token_bytes(),
            xsrf_cookies=True,
            login_url="/login/",
            template_path=BASE_DIR / "templates",
        )
        super().__init__(handlers, **settings)


if __name__ == "__main__":
    App().listen(8000)
    IOLoop.current().start()
