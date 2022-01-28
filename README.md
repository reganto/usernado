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
```



As you can see `Handler` is a Facade. you can use it to handle your request as you wish.

## TODO

- [ ] str_plural uimodule
- [ ] send and broadcast for websockets


