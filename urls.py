from tornado.web import url
from handlers.home import HomeHandler

url_patterns = [
    url(r"/", HomeHandler, name='home'),
]
