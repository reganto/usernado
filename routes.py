import handlers 
from tornado.web import url

ROUTES = [
    url('/', handlers.homePageHandler, name='home'),
]

