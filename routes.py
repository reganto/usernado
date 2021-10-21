from tornado.web import url

import views

routes = [
    url('/', views.HomePageHandler, name='home'),
]

