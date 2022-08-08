import secrets
from pathlib import Path

from tornado.ioloop import IOLoop
from tornado.web import Application, url

from usernado import Usernado

BASE_DIR = Path(__file__).resolve().parent


class HomeHandler(Usernado.Web):
    def get(self):
        self.render("sock.html")


class EchoConnection(Usernado.WebSocket):
    def on_message(self, message):
        self.send(message)
        # Use send.broadcast(msg) to send message to all participants


class App(Application):
    def __init__(self):
        handlers = [
            url("/", HomeHandler),
            url("/echo", EchoConnection),
        ]
        settings = dict(
            debug=True,
            template_path=BASE_DIR / "templates",
            cookie_secret=secrets.token_bytes(),
        )
        super().__init__(handlers, **settings)


if __name__ == "__main__":
    App().listen(8000)
    IOLoop.current().start()
