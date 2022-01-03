import tornado.web
import tornado.ioloop
from tornado.options import parse_command_line

from routes import ROUTES 
from config import SETTINGS


class Application(tornado.web.Application):
    def __init__(self):
        super().__init__(ROUTES, **SETTINGS)


if __name__ == '__main__':
    parse_command_line()
    Application().listen(8000)
    tornado.ioloop.IOLoop.current().start()

