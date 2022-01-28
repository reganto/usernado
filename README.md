# Usernado

[Tornado](https://www.tornadoweb.org/en/stable/) Boilerplate for Human 

## So Far

* **Handler Facade:** Api, Web, WebSocket
* **Api:** get_json_argument(s)
* **Web:** redirect_to_route
* **testing:** login



## Examples

**Web**:

```python
from .usernado import Handler



class Hello(Handler.Web):
    def get(self):
        self.render('hello.html')
```



**Api**

```python
from .usernado import Handler



class Echo(Handler.Api):
    def get(self):
        username = self.get_json_argument('username')
        self.write({'username': username})
```



**WebSocket**

```python
from .usernado import Handler



class Echo(Handler.WebSocket):
    def on_message(self, message):
        self.send(message)
        # Use send to send message to specific participant
        # And use broadcast to send message to participants
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

- [ ] str_plural uimodule
- [ ] send and broadcast for websockets


