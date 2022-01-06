from tornado.web import url
from handlers.home import homeHandler

ROUTES = [
    url('/', homeHandler, name='home'),
]

