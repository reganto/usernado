from views.base import BaseHandler


class HomePageHandler(BaseHandler):
    def get(self):
        self.render('home.html')
