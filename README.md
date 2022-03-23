Usernado is a [Tornado](https://www.tornadoweb.org/en/stable/) extension to make life easier.

## Installation

You can install Usernado as usual with pip:

```bash
pip install usernado
```

## Example

```python
from usernado import Handler

# Create User model in advance
from database.models import User


class RegisterUser(Handler.Web):
    def get(self):
        self.render("register.html")

    def post(self):
        username = self.get_escaped_argument("username")
        password = self.get_escaped_argument("password")

        self.register(User, username, password)
```

As you see `Handler` is a Facade. you can use it to handle your requests as you wish.

## Resources

- [Documentation](#)

- [Examples](https://github.com/reganto/Usernado/tree/master/example)

- [PyPI](https://pypi.org/project/usernado/)

- [Change Log](https://github.com/reganto/Usernado/blob/master/CHANGES.md)

## TODO

- [x] Send and broadcast for websockets
- [x] Abstracted authentication methods
- [ ] Authenticaion methods should return True/False
- [ ] Add username & password to test login 
- [ ] Add pluralize (str_plural) uimodule
- [ ] Add diff_for_human (humanize) decorator
- [ ] Add third party authentication abstract methods
- [ ] Add pagination
