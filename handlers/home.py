from .base import BaseHandler


class homePageHandler(BaseHandler):
    def get(self):
        self.render('home.html')

