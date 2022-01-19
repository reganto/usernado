import json

from .usernado import Handler


class IndexHandler(Handler.Web):
    def get(self):
        self.render('index.html')


class UsersHandler(Handler.Api):
    def post(self):
        try:
            username = self.get_json_argument('username')
            self.write({'username': username})
        except json.decoder.JSONDecodeError as e:
            self.write('Error: Json argument does not exist in current request.')
