from .usernado import Handler

class IndexHandler(Handler.Web):
    def get(self):
        self.render('index.html')

