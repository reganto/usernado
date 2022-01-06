from .usernado import Handler

class homeHandler(Handler.Web):
    def get(self):
        self.render('home.html')

