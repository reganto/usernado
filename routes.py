from tornado.web import url
from handlers.home import IndexHandler

ROUTES = [
    url('/', IndexHandler, name='index'),
]

