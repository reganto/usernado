<a id="top"></a>
<br />

<div align="center">
  <h1>Usernado</h1>
  <p align="center">
    A Tornado Extension to Make Life Easier.
    <br />
    <a href="#"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/reganto/Usernado/tree/master/example">View Demo</a>
    ·
    <a href="https://github.com/reganto/Usernado/issues">Report Bug</a>
    ·
    <a href="https://github.com/reganto/Usernado/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#why-usernado">Why Usernado</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#installation">Installation</a></li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#example">Example</a></li>
        <li><a href="#resources">Resources</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- Why Userndo  -->

## Why Usernado

I'm using Tornado every day. I really like it. Besides of all advantages of Tornado, it's not a full-stack framework, and I had to put all the pieces of the puzzle together every day! So this is my attempt to follow DRY(Don't Repeat Yourself) principle. this is how the Usernado was born.

<!-- Features -->

## Features

- REST support

- Websocket easier than ever

- ORM agnostic authentication

- Humanize datetime in templates

- Better exception printer thanks to [tornado-debugger](https://github.com/bhch/tornado-debugger)

<!-- Getting Started -->

## Installation

Install either with pip or poetry.

```bash
pip install usernado
or
poetry add usernado
```

Or optionally you can install from github using `pip install git+https://github.com/reganto/usernado`

<!-- USAGE EXAMPLES -->

## Usage

### Example

```python
from usernado import Usernado


class HelloHandler(Usernado.Web):
    def get(self):
        self.write("Hello, World!")
```

For more examples please Check out [examples](https://github.com/reganto/Usernado/tree/master/example).

### Resources

- [Documentation](#)

- [PyPI](https://pypi.org/project/usernado/)

- [Change Log](https://github.com/reganto/Usernado/blob/master/CHANGES.md)

<!-- ROADMAP -->

## Roadmap

- [x] Send and broadcast for websockets
- [x] Abstracted authentication methods
- [x] Authenticaion methods should return True/False
- [x] Add diff_for_human (humanize) decorator
- [x] Add api_route for API handlers
- [x] Add username & password to test login 
- [x] Add pluralize (str_plural) uimodule
- [ ] Add third party authentication abstract methods
- [ ] Add pagination

See the [open issues](https://github.com/reganto/Usernado/issues) for a full list of proposed features (and known issues).

<!-- LICENSE -->

## License

Distributed under the Apache License. See `LICENSE.txt` for more information.

<!-- CONTACT -->

## Contact

Email: tell.reganto[at]gmail[dotcom]

<p align="right">(<a href="#top">back to top</a>)</p>
