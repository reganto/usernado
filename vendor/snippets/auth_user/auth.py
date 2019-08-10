import uuid
import base64
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpserver
import tornado.escape

from tornado.options import options, define
define("port", default=8888, help="run on the given port", type=int)

from tornado.web import url

from mysql.connector import MySQLConnection, Error
from argon2 import PasswordHasher, exceptions
ph = PasswordHasher()

from python_mysql_dbconfig import read_db_config


class Appliaction(tornado.web.Application):
    def __init__(self):
        try:
            db_config = read_db_config()
            self.conn = MySQLConnection(**db_config)
        except Error as e:
            print(e)
        urlpatterns = [
            url(r"/", HomeHandler, name="home"),
            url(r"/auth/register", RegisterHandler, name="register"),
            url(r"/auth/login", LoginHandler, name="login"),
        ]
        settings = dict(
            debug=True,
            cookie_secret=base64.b64encode(uuid.uuid4().bytes+uuid.uuid4().bytes)
        )
        super().__init__(urlpatterns, **settings)


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user = self.get_secure_cookie('user')
        if user:
            return tornado.escape.json_decode(user)
        else:
            return None



class HomeHandler(BaseHandler):
    def get(self):
        self.write(
            '''<a href="{}">Login</a><br />'''
            '''<a href="{}">SignUp</a>'''.format(
                self.reverse_url('login'),
                self.reverse_url('register')
                )
        )


class RegisterHandler(BaseHandler):
    def initialize(self):
        self.conn = self.application.conn
        self.cursor = self.conn.cursor()

    def prepare(self):
        if "Firefox" in self.request.headers['User-Agent']:
            pass
        else:
            self.redirect(self.reverse_url('home'))

    def get(self):
        self.write(
            ''' <html><body><form method="POST" enctype="multipart/form-data"> '''
            ''' <input type="text" name="username" placeholder="username" /><br /> '''
            ''' <input type="password" name="password" placeholder="password" /><br /> '''
            ''' <input type="email" name="email" placeholder="email" /><br /> '''
            ''' <input type="file" name="image" accept="image/png" /><br /> '''
            ''' <input type="submit" value="Register" /> '''
        )
    
    def post(self):
        username = self.get_body_argument('username', '')
        password = self.get_body_argument('password', '')
        email = self.get_body_argument('email', '')
        photo = self.request.files['image'][0]['body']
        
        # check connection to db
        if self.conn.is_connected():
            query = "SELECT username FROM users WHERE username = %s"
            self.cursor.execute(query, (username, ))
        else:
            self.write('Connection to database was not established!!!!')
        
        if self.cursor.fetchone() is None:
            # encode password to UTF-8
            password = password.encode('utf-8')
            # generate salt and encode it
            salt = uuid.uuid4().hex.encode('utf-8')

            hashed_password = ph.hash(password+salt)
            
            # insert user info in database
            query = """ INSERT INTO users (username, password, email, salt, photo)
                    Values(%s,%s,%s,%s,%s)
                    """
            args = (username, hashed_password, email, salt, photo)
            self.cursor.execute(query, args)

            self.conn.commit()
            
            self.redirect(self.reverse_url('login'))
        else:
            self.write('This username already exist')
    
    # def on_finish(self):
    #     self.cursor.close()
    #     self.conn.close()


class LoginHandler(BaseHandler):
    def initialize(self):
        self.conn = self.application.conn
        self.cursor = self.conn.cursor()

    def prepare(self):
        if 'Firefox' in self.request.headers['User-Agent']:
            pass
        else:
            self.redirect(self.reverse_url('home'))
    
    def get(self):
        self.write(
            ''' <html><body><form method="POST" enctype="multipart/form-data"> '''
            ''' <input type="text" name="username" placeholder="username" /><br /> '''
            ''' <input type="password" name="password" placeholder="password" /><br /> '''
            ''' <input type="submit" value="Login" /> '''
        )
    
    def post(self):
        username = self.get_body_argument('username', '')
        password = self.get_body_argument('password', '')

        query = "SELECT username, password, salt, email FROM users " \
                "WHERE username = %s"
        self.cursor.execute(query, (username, ))

        user_exists = False
        try:
            result = self.cursor.fetchone()
            if result is None:
                raise TypeError()
        except TypeError:
            self.write('User does not exists')
        else:
            email = result[3]
            saved_password = result[1]
            saved_salt = result[2].encode('utf-8')
            password = password.encode('utf-8')
            user_exists = True

        if user_exists:
            try: 
                ph.verify(saved_password, password+saved_salt)
            except exceptions.VerifyMismatchError:
                self.write({'status': 'Password is incorrect'})
            else:
                self.write({'status': 'ok'})
                self.set_secure_cookie('user', tornado.escape.xhtml_escape(email))
            
    # def on_finish(self):
    #     self.cursor.close()
    #     self.conn.close()
    

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Appliaction())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()

