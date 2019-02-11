Tornado with extra tools
========================

[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://www.python.org/)
[![Tornado Version](https://img.shields.io/badge/version-5.1.1-brightgreen.svg)](https://www.tornadoweb.org/en/stable/)

## Description

[Tornado](https://github.com/tornadoweb/tornado) is a powefull and light weight python framework.BUT tornado haven't any boilerplate so you must start your project from scratch also tornado haven't post redirection(redirection with parameter(s) in post method).now these features are available.

Tools : 

* [tornado-boilerplate](https://github.com/reganto/tornado-boilerplate)
* [post redirection](https://github.com/reganto/paratorn)

## Directory Structure

    tornado/
        handlers/
            home.py
            base.py
        logconfig/
        media/
            css/
                vendor/
            js/
                vendor/
            images/
        requirements/
            common.txt
            dev.txt
            production.txt
        templates/
            assets/
                base.html
                hide.html
            home/
                index.html
        vendor/
            redirect.py
        environment.py
        fabfile.py
        app.py
        settings.py


#### How to

First install Tornado
```bash
    pip install tornado
```
* It it better to install Tornado in virtualenv

* You should already install git

Copy tornado directory to your local disk.

Go to tornado directory.

Run this command in bash:
```bash
    sudo ./configure.sh
```

Now you can create a new project with this command:
```bash
    tornado project-name
```

Go to project directory.

For run server type this command in bash:
```bash
    python app.py --port=favorite-port  
```

* If you want to use post redirection:
```python
    from vendor import redirect  
```

then your class must inherite from `redirect.BaseHandler`

in class method use `self.redirect_with_input()`


## Contributing

If you have improvements or bug fixes:

* Fork the repository on GitHub
* File an issue for the bug fix/feature request in GitHub
* Create a topic branch
* Push your modifications to that branch
* Send a pull request

## Authors

* [Reganto Blog](http://www.reganto.blog.ir)
* [Reganto Github](https://github.com/reganto/)
