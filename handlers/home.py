from .usernado import Handler


class Home(Handler.Web):
    def get(self):
        if self.authenticate():
            self.render('home.html')
        else:
            self.write('<h3>Your not an authenticated user, login first.</h3>')
