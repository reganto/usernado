import tornado.web
import tornado.escape


class APIHandler(tornado.web.RequestHandler):

    def get_json_argument(self, name, default=None):  # TODO: needs refactoring! here is lack of Docstring and Logic is pice of sheet
        if self.request.body:
            try:
                raw_data = self.request.body.decode().replace('\'', '\"')
                json_data = tornado.escape.json_decode(raw_data)
                return json_data.get(name, default)
            except Exception as e:
                print('Error in get_json_argument: ', e)
        else:
            print('Data is not presented')

    def get_json_arguments(self):  # TODO: needs refactoring! here is lack of Docstring and Logic is pice of sheet
        if self.request.body:
            try:
                raw_data = self.request.body.decode().replace('\'', '\"')
                json_data = tornado.escape.json_decode(raw_data)
                return json_data
            except Exception as e:
                print('Error in get_json_argument: ', e)
        else:
            print('Data is not presented')

