from .usernado import Handler


import peewee

db = peewee.SqliteDatabase('db.sqlite3')

class BaseModel(peewee.Model):
    class Meta:
        database = db


class User(BaseModel):
    username = peewee.CharField(
        max_length=255, 
        unique=True,
        )
    password = peewee.CharField(max_length=255)
    salt = peewee.CharField(max_length=100)

db.create_tables([User, ], safe=True)


class Register(Handler.Web):
    def get(self):
        self.render('auth/register.html')

    def post(self):
        username = self.get_scaped_argument('username')
        password = self.get_scaped_argument('password')

        self.register(User, username, password)


class Login(Handler.Web):
    def get(self):
        self.render('auth/login.html')

    def post(self):
        username = self.get_scaped_argument('username')
        password = self.get_scaped_argument('password')

        try:
            self.login(User, username, password)
        except PermissionError as e:
            self.write('Username or password is incorrect!')


class Logout(Handler.Web):
    def get(self):
        if self.authenticate():
            self.logout()
        else:
            self.write('<h3>Your not an authenticated user, login first.</h3>')
