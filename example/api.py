from tornado.ioloop import IOLoop
from tornado.web import Application

from usernado import APIHandler
from usernado.helpers import api_route


@api_route("/api/v1.3/echo/")
class EchoHandler(APIHandler):
    def post(self):
        message = self.get_json_argument("message")
        self.write(message)


class App(Application):
    def __init__(self):
        super().__init__(api_route.urls, debug=True)


if __name__ == "__main__":
    App().listen(8000)
    IOLoop.current().start()


"""
curl -X POST \
-i http:/localhost:8000/api/v1.3/echo/ \
-H "Content-Type:application/json" \
-d "{'message': 'Hello'}"
"""
