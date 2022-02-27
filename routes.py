from tornado.web import url
from handlers import Home

ROUTES = [
    url('/', Home, name='home'),
]
