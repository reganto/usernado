from usernado.helpers import api_route
from tornado.web import Application
from tornado.ioloop import IOLoop
from usernado import Handler


@api_route("/", "home")
class Home(Handler.API):
    def get(self):
        self.write({"message": "Hello"})


class App(Application):
    def __init__(self):
        super().__init__(api_route.urls, debug=True)


if __name__ == "__main__":
    App().listen(8000)
    IOLoop.current().start()
