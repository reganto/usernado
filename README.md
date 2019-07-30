# Tornado
[![Python Version](https://img.shields.io/badge/python-3.7.4-green)](https://www.python.org/)
[![Tornado Version](https://img.shields.io/badge/tornado-6.0.3-green)](https://www.tornadoweb.org/en/stable/)

## Description

[Tornado](http://www.tornadoweb.org/en/stable/) is a powerfull and lightweight python framework. But tornado haven't any template so you must start your project from scratch also tornado haven't post redirection(redirection with parameter(s) in post method). now these features are available!


- See also [Tornado-utilities](https://gitlab.com/reganto/tornado-utilities)


## How to

First install dependencies from requirements.txt 

    pip install -r requirements.txt

* It it better to install dependencies in virtualenv

* You should already install git

Clone repository to your local disk.

    git clone https://gitlab.com/reganto/tornado
    or
    git clone https://github.com/reganto/tornado


Go to tornado directory.

Run this command in bash:

    sudo ./configure.sh

Now you can create a new project with this command:

    tornado project-name

Go to project directory.

To show help

    python app.py --help

* If you want to use post redirection:

  Your class must inherite from `BaseHandler`

```python
    from handlers.base import BaseHandler
```

in class method use `self.redirect_with_input()`

## TODO

- [x] Update jquery
- [x] Add w3.css
- [x] Remove requirements directory and add single requirements file
- [x] Add settings to choose template engine
- [x] Add error page for tornado template
- [ ] Add error page for jinja2 template
- [ ] Edit explanations
- [ ] Tornado  utility should support other OS (now support *\*nix*)
- [ ] Add paginatoin snippet
- [ ] Add upload snippet
- [ ] Add register snippet
- [ ] Add login snippet

## Contributing

If you have improvements or bug fixes:

* Fork the repository on GitHub or GitLab
* File an issue for the bug fix/feature request in GitHub GitLab
* Create a topic branch
* Push your modifications to that branch
* Send a pull request

## Author

* [Reganto Blog](http://www.reganto.blog.ir)
* [Reganto GitLab](https://gitlab.com/reganto/)
* [Reganto GitHub](https://github.com/reganto/)

