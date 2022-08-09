from pathlib import Path
import secrets

from tornado.ioloop import IOLoop
from tornado.web import Application, url

from usernado import WebHandler
from usernado.helpers import Pluralize

BASE_DIR = Path(__file__).resolve().parent


class ReplyController(WebHandler):
    def get(self):
        reply_counter = 2
        self.render("pluralize_uimodule.html", reply_counter=reply_counter)


class App(Application):
    def __init__(self):
        handlers = [url("/", ReplyController)]
        settings = dict(
            debug=True,
            ui_modules=dict(pluralize=Pluralize),
            cookie_secret=secrets.token_bytes(),
            template_path=BASE_DIR / "templates",
        )
        super().__init__(handlers, **settings)


if __name__ == "__main__":
    App().listen(8000)
    IOLoop.current().start()
