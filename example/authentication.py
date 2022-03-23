import secrets
from pathlib import Path

import peewee
from tornado.ioloop import IOLoop
from tornado.web import Application, authenticated, url
from usernado import Handler


BASE_DIR = Path(__file__).resolve().parent

# You can use either Peewee or Sqlalchemy as ORM
DB = peewee.SqliteDatabase("db.sqlite3")


class User(peewee.Model):
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


class RegisterHandler(Handler.Web):
    def get(self):
        self.render("register.html")

    def post(self):
        username = self.get_escaped_argument("username")
        password = self.get_escaped_argument("password")
        try:
            self.register(User, username, password)
        except Exception as e:
            print(e)
        else:
            self.redirect_to_route("login")


class LoginHandler(Handler.Web):
    def get(self):
        self.render("login.html")

    def post(self):
        username = self.get_escaped_argument("username")
        password = self.get_escaped_argument("password")
        try:
            self.login(User, username, password)
        except Exception as e:
            print(e)
        else:
            self.redirect_to_route("dashboard")


class LogoutHandler(Handler.Web):
    def get(self):
        if self.authenticate():
            self.logout()
        self.redirect_to_route("login")


class DashboardHandler(Handler.Web):
    @authenticated
    def get(self):
        self.write("Dashborad")


class App(Application):
    def __init__(self):
        handlers = [
            url("/", DashboardHandler, name="dashboard"),
            url("/register/", RegisterHandler, name="register"),
            url("/login/", LoginHandler, name="login"),
            url("/logout/", LogoutHandler, name="logout"),
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