from pathlib import Path
import secrets

from tornado.ioloop import IOLoop
from tornado.web import Application, url

from usernado import WebHandler, WebSocketHandler

BASE_DIR = Path(__file__).resolve().parent


class HomeHandler(WebHandler):
    def get(self):
        self.render("sock.html")


class EchoConnection(WebSocketHandler):
    def on_message(self, message):
        self.send(message)
        # Use send.broadcast(msg) to send message to all participants


class App(Application):
    def __init__(self):
        handlers = [
            url("/", HomeHandler),
            url("/echo", EchoConnection),
        ]
        settings = {
            "debug": True,
            "template_path": BASE_DIR / "templates",
            "cookie_secret": secrets.token_bytes(),
        }
        super().__init__(handlers, **settings)


if __name__ == "__main__":
    App().listen(8000)
    IOLoop.current().start()
