from handlers.usernado import Handler


class Home(Handler.Web):
    def get(self):
        self.render('home.html')
