Tornado with extra tools
===============================================================================

## Description

Tools : 

* awesome [tornado-boilerplate](https://github.com/reganto/tornado-boilerplate)
* post redirection

### Related Projects

[tornado](https://github.com/reganto/tornado)
[paratorn](https://github.com/reganto/paratorn)

## Directory Structure

    tornado-boilerplate/
        handlers/
            home.py
            base.py
        lib/
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
        utilities/
            redirect.py
        environment.py
        fabfile.py
        app.py
        settings.py


#### Who to
install tornado
```sh
    pip install tornado
```
for run server 
```sh
    python app.py --port=8888
```
if you want to use post redirection 
```python
    from utilities import redirect
```
then your class must inherite from `redirect.RequestHandler`

in class method use `self.redirect_with_input()`

## Contributing

If you have improvements or bug fixes:

* Fork the repository on GitHub
* File an issue for the bug fix/feature request in GitHub
* Create a topic branch
* Push your modifications to that branch
* Send a pull request

## Authors

* [Reganto](http://www.reganto.blog.ir)
* [gitlab](https://gitlab.com/reganto/)
* [github](https://github.com/reganto/)
