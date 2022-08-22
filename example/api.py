from tornado import ioloop, web

from usernado import APIHandler, api_route


@api_route("/api/v1.3/echo/")
class EchoHandler(APIHandler):
    def post(self):
        message = self.get_json_argument("message")
        self.write(message)


def make_app():
    return web.Application(api_route.urls)


def main():
    app = make_app()
    app.listen(8000)
    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()


"""
curl -X POST \
-i http:/localhost:8000/api/v1.3/echo/ \
-H "Content-Type:application/json" \
-d "{'message': 'Hello'}"
"""
