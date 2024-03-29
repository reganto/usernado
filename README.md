<a id="top"></a>
<br />

<div align="center">
  <h1>Usernado</h1>
  <p align="center">
    Makes it Easy to Manage Tornado :tornado: Applications
    <br />
    <a href="https://usernado.readthedocs.io/en/latest/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/reganto/usernado/actions?query=workflow%3Abuild+event%3Apush+branch%3Amaster" target="_blank">
    <img src="https://github.com/reganto/usernado/workflows/Linters/badge.svg?event=push&branch=master" alt="Test">
    </a>
    <a href="https://github.com/reganto/Usernado/issues"><img src="https://img.shields.io/github/issues/reganto/usernado"></a> <a href="https://github.com/reganto/usernado/blob/master/LICENSE.txt"><img src="https://img.shields.io/github/license/reganto/usernado"></a>  <a href="https://badge.fury.io/py/usernado"><img src="https://badge.fury.io/py/usernado.svg" alt="PyPI version" height="18"></a> <a href="https://pepy.tech/project/usernado"><img src="https://pepy.tech/badge/usernado"/></a>
  </p>
</div>

<!-- Why Userndo  -->

## Why Usernado

- Why not?

- I like :tornado:

- For every project I wrote with Tornado, I had to repeat the code for some parts. For example, to authenticate users, I had to write repeated code every time. So I decided to write an extension to solve my need.

<!-- Features -->

## Features

- REST support :zap:

- Websocket easier than ever :zap:

- ORM agnostic authentication :zap:

- Humanize datetime in templates :zap:

- Better exception printer thanks to [tornado-debugger](https://github.com/bhch/tornado-debugger) :zap:

<!-- Getting Started -->

## Installation

Install either with pip or poetry.

```bash
pip install usernado
```
```bash
poetry add usernado
```

Or optionally you can install from github using 
```bash 
pip install git+https://github.com/reganto/usernado
```

<!-- USAGE EXAMPLES -->

## Usage

### Hello Usernado

```python
from usernado.helpers import api_route
from usernado import APIHandler
from tornado import web, ioloop


@api_route("/hello", name="hello")
class Hello(APIHandler):
    def get(self):
        self.response({"message": "Hello, Usernado"})

def make_app():
    return web.Application(api_route.urls, autoreload=True)


def main():
    app = make_app()
    app.listen(8000)
    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
```

For more examples please Check out [examples](https://github.com/reganto/Usernado/tree/master/example).

<!-- ROADMAP -->

## Roadmap

- [x] Send and broadcast for websockets
- [x] Abstracted authentication methods
- [x] Authenticaion methods should return True/False
- [x] Add diff_for_human (humanize) decorator
- [x] Add api_route for API handlers
- [x] Add username & password to test login 
- [x] Add pluralize (str_plural) uimodule
- [x] Add pagination [:link:](https://github.com/reganto/tornado-pagination)

<!-- CONTACT -->

## Open your mailbox and 
tell.reganto[at]gmail.com

Hello!

<p align="right"><a href="#top"><img src="https://raw.githubusercontent.com/DjangoEx/python-engineer-roadmap/main/statics/top.png" width=50 height=50 /></a></p>
