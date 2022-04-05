from datetime import datetime
import secrets

from usernado.helpers import humanize
from tornado.web import Application
from tornado.ioloop import IOLoop
from usernado import Handler
import peewee


DB = peewee.SqliteDatabase("db.sqlite3")


class Post(peewee.Model):
    title = peewee.CharField(max_length=100)
    created_at = peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = DB

    @humanize
    def diff_for_humans(self):
        return self.created_at


DB.create_tables(
    [
        Post,
    ],
    safe=True,
)


class Home(Handler.Web):
    def get(self):
        posts = Post.select()
        self.render("humanize.html", posts=posts)


if __name__ == "__main__":
    Application(
        [("/", Home)],
        debug=True,
        cookie_secret=secrets.token_bytes(),
        template_path="templates",
    ).listen(8000)
    IOLoop.current().start()
