import tornado.web
import tornado.ioloop
from tornado.options import parse_command_line

from routes import routes as Routes
from settings import settings as Settings


def _settings_to_dict(cls):
    class_attributes_dict = vars(cls)
    result_dict = {}
    for key, value in class_attributes_dict.items():
        if not key.startswith('__'):
            result_dict[key] = value
    return result_dict


class Application(tornado.web.Application):
    def __init__(self):
        routes = Routes
        settings = _settings_to_dict(Settings.get('development'))
        super().__init__(routes, **settings)


if __name__ == '__main__':
    parse_command_line()
    Application().listen(8001)
    tornado.ioloop.IOLoop.current().start()
