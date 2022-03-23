import secrets
from pathlib import Path

from tornado.web import Application, url
from tornado.ioloop import IOLoop
from usernado import Handler


BASE_DIR = Path(__file__).resolve().parent


class Home(Handler.Web):
    def get(self):
        self.render("sock.html")


class Echo(Handler.WebSocket):
    def on_message(self, message):
        self.send(message)


class App(Application):
    def __init__(self):
        handlers = [
            url("/", Home),
            url("/echo", Echo),
        ]
        settings = dict(
            debug=True,
            template_path = BASE_DIR / "templates",
            cookie_secret= secrets.token_bytes(),
        )
        super().__init__(handlers, **settings)


if __name__ == "__main__":
    App().listen(8000)
    IOLoop.current().start()

