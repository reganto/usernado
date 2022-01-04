from .usernado import Facade

class homePageHandler(Facade.webHandler):
    def get(self):
        self.render('home.html')

