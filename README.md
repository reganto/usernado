# Usernado

[Tornado](https://www.tornadoweb.org/en/stable/) Boilerplate for Human 

## Hello World

```python
from handlers.usernado import Handler


class HelloWorld(Handler.Web):
    def get(self):
        self.write('Hello, World!')
```

As simple as possible, isn't it?

## Install Usernado 

```bash
git clone https://github.com/reganto/Usernado.git
```

## Authentication Example

**Register User**:

```python
from handlers.usernado import Handler
#  you should make User model in advance
from database.models import User


class RegisterUser(Handler.Web):
    def get(self):
        self.render('register.html')

    def post(self):
        username = self.get_escaped_argument('username')
        password = self.get_escaped_argument('password')

        self.register(User, username, password)
```

**Login User**

```python
from handlers.usernado import Handler
#  you should make User model in advance
from database.models import User


class LoginUser(Handler.Web):
    def get(self):
        self.render('login.html')

    def post(self):
        username = self.get_escaped_argument('username')
        password = self.get_escaped_argument('password')

        self.login(User, username, password)
```

**Logout User**

```python
from handlers.usernado import Handler


class LogoutUser(Handler.Web):
    def get(self):
        if self.authenticate():
            self.logout()
        else:
            self.write('<h3>You are not an authenticated user.</h3>')
```

## API Example

```python
from handlers.usernado import Handler


class Echo(Handler.Api):
    def get(self):    
        message = self.get_json_argument('message')
        self.write({'message': message})
```

## Websocket Example

```python
from handlers.usernado import Handler


class Echo(Handler.WebSocket):
    def on_message(self, message):
        self.send(message)
```

As you see `Handler` is a Facade. you can use it to handle your requests as you wish.

## TODO

- [x] Send and broadcast for websockets
- [x] Abstracted authentication methods
- [ ] Authenticaion methods should return True/False
- [ ] Add username & password to test login 
- [ ] Add pluralize (str_plural) uimodule
- [ ] Add diff_for_human (humanize) decorator
- [ ] Add third party authentication abstract methods
- [ ] Add pagination
