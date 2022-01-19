from tornado.web import url
from handlers.home import IndexHandler, UsersHandler

ROUTES = [
    url('/', IndexHandler, name='index'),
    url('/users', UsersHandler, name='users'),
]
