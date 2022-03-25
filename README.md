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
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#example">Example</a></li>
        <li><a href="#resources">Resources</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- Getting Started -->

## Getting Started

### Features

- REST support

- Websocket easier than ever

- ORM agnostic authentication

- Humanize datetime in templates

- Better exception printer thanks to [tornado-debugger](https://github.com/bhch/tornado-debugger)


### Installation

Install it via pip:

```bash
pip install usernado
```

<!-- USAGE EXAMPLES -->

## Usage

### Example

```python
from usernado import Handler



class Echo(Handler.API):
    def post(self):
        message = self.get_json_argument("message")
        self.write({"message": message})
```

### Resources

- [Documentation](#)

- [Examples](https://github.com/reganto/Usernado/tree/master/example)

- [PyPI](https://pypi.org/project/usernado/)

- [Change Log](https://github.com/reganto/Usernado/blob/master/CHANGES.md)

<!-- ROADMAP -->

## Roadmap

- [x] Send and broadcast for websockets
- [x] Abstracted authentication methods
- [x] Authenticaion methods should return True/False
- [ ] Add username & password to test login 
- [ ] Add pluralize (str_plural) uimodule
- [ ] Add diff_for_human (humanize) decorator
- [ ] Add third party authentication abstract methods
- [ ] Add pagination

See the [open issues](https://github.com/reganto/Usernado/issues) for a full list of proposed features (and known issues).

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->

## Contact

Project Link: [https://github.com/reganto/Usernado](https://github.com/reganto/Usernado)

Email: [tell.reganto](mailto:tell.reganto@gmail.com)

<p align="right">(<a href="#top">back to top</a>)</p>
