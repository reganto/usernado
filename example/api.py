from tornado.web import Application, url
from tornado.ioloop import IOLoop
from usernado import Handler


class EchoHandler(Handler.API):
    def post(self):
        message = self.get_json_argument("message")
        self.write({"message": message})


if __name__ == "__main__":
    Application([(r"/echo/", EchoHandler)]).listen(8000)
    IOLoop.current().start()


"""
curl -X POST \
-i http:/localhost:8000/echo/ \
-H "Content-Type:application/json" \
-d "{'message': 'Hello'}"
"""

