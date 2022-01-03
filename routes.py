from tornado.web import url

import handlers 

ROUTES = [
    url('/', handlers.homePageHandler, name='home'),
]

