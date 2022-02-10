# Usernado

[Tornado](https://www.tornadoweb.org/en/stable/) Boilerplate for Human 

## Hello World

```python
from .usernado import Handler



class HelloWorld(Handler.Web):
    def get(self):
        self.write('Hello, World!')
```

You should add a route for `HelloWorld` handler to rotues.py file.

## Examples

**Register User**:

```python
from models import User
from .usernado import Handler


class RegisterUser(Handler.Web):
    def get(self):
        self.render('register.html')

    def post(self):
        username = self.get_scaped_argument('username')
        password = self.get_scaped_argument('password')
        
        self.register(User, username, password)
```

**Login User**

```python
from models import User
from .usernado import Handler


class LoginUser(Handler.Web):
    def get(self):
        self.render('register.html')

    def post(self):
        username = self.get_scaped_argument('username')
        password = self.get_scaped_argument('password')
        
        self.login(User, username, password)
```

**Logout User**

```python
from .usernado import Handler


class LogoutUser(Handler.Web):
    def get(self):
        if self.authenticate():
            self.logout()
        else:
            self.write('<h3>You are not an authenticated user.</h3>')
```

You should create a models.py file and define a `User` model.

**Api**

```python
from .usernado import Handler


class Echo(Handler.Api):
    def get(self):    
        message = self.get_json_argument('message')
        self.write({'message': message})
```

As simple as possible. Isn't it?

**WebSocket**

```python
from .usernado import Handler



class Echo(Handler.WebSocket):
    def on_message(self, message):
        self.send(message)
```

As you can see `Handler` is a Facade. you can use it to handle your request as you wish.

## Login test user

if you want an authenticated user in your tests so try `login` method. below is a example:

```python
from tests.base import BaseTestCase



class YourTestCase(BaseTestCase):
    def test_an_authenticated_user_can_see_threads(self):
        headers = self.login('/users/login')
        # Use headers in your further request
        # Note: if you use login method to authenticate user
        # and then try to send some headers with forther request
        # you have to append your headers to headers that comes from
        # login method. Umm something like headers.update(your_headers).

        response = self.fetch(
            '/threads/',
            method='GET',
            headers=headers
            )

         self.assertEqual(response.code, 200)
```

## TODO

- [x] Send and broadcast for websockets
- [ ] Abstracted authenticate methods
- [ ] pluralize uimodule
