import tornado.web


class WebHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie('username')

    def redirect_to_route(self, name: str):
        self.redirect(self.reverse_url(name))

