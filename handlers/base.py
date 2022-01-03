import tornado.web
import tornado.escape


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('user')

    def get_json_argument(self, name, default=None):
        if self.request.body:
            try:
                raw_data = self.request.body.decode().replace('\'', '\"')
                json_data = tornado.escape.json_decode(raw_data)
                return json_data.get(name, default)
            except Exception as e:
                print('Error in get_json_argument: ', e)
        else:
            print('Data is not presented')

    def get_json_arguments(self):
        if self.request.body:
            try:
                raw_data = self.request.body.decode().replace('\'', '\"')
                json_data = tornado.escape.json_decode(raw_data)
                return json_data
            except Exception as e:
                print('Error in get_json_argument: ', e)
        else:
            print('Data is not presented')

