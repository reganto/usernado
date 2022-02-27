from unicodedata import name
from tornado.web import url
from handlers import Home, Register, Login, Logout

ROUTES = [
    url('/', Home, name='home'),
    url('/auth/register/', Register, name='register'),
    url('/auth/login/', Login, name='login'),
    url('/auth/logout/', Logout, name='logout'),
]
