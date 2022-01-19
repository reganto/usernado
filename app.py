import tornado.web
import tornado.ioloop
import tornado.options
from routes import ROUTES 
from config import SETTINGS


class Application(tornado.web.Application):
    def __init__(self):
        super().__init__(ROUTES, **SETTINGS)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    Application().listen(8000)
    tornado.ioloop.IOLoop.current().start()
