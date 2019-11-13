<p align="center">
    <img src="https://user-images.githubusercontent.com/29402115/63076666-38541e00-bf4b-11e9-9b19-9e25c9b268cb.png" 
         width="300" height="300" />
</p>


---
![Usernado](https://img.shields.io/badge/usernado-1.1.0-green)
![License](https://img.shields.io/hexpm/l/plug?color=green)

### Features

- Send  arguments to other request without session(special thanks to Ehsan Azizi Khadem and [Ben Darnell](https://github.com/bdarnell))
- Tornado-boilerplate -- a standard layout for Tornado apps(thanks to [Bueda](https://github.com/bueda/tornado-boilerplate))
- Add Jinja2 template engine(thanks to [mr-ping](https://github.com/mr-ping/tornado_jinja2))
- Better error page
- Startup configuration bash script
- A utility to create new project
- Utilities(utils/)
- Code snippets(I decided to create a new repository to make the Usernado lighter -> [here](https://github.com/reganto/tornado-snippets))


## How to


![whoto](https://user-images.githubusercontent.com/29402115/63206974-0f12c980-c0d4-11e9-815a-b513e2aadc6c.gif)


First install Tornado:

    pip install tornado

* It it better to install dependencies in virtualenv


Clone repository to your local disk.

    git clone https://github.com/reganto/usernado.git


Go to Usernado directory.

Run following command in bash:

    sudo ./configure

Now you can create a new project with `usernado` command:

    usernado project-name

Go to project directory.


* If you want to send  arguments to other request without session:

  Your class must inherite from `BaseHandler`

```python
    from handlers.base import BaseHandler
```

in class method use `self.redirect_with_input()`

## Related Projects

- **[Motor](https://github.com/mongodb/motor)**  -> The async Python driver for MongoDB and Tornado or asyncio 
- **[Tornado-Jinja2](https://github.com/mr-ping/tornado_jinja2)** -> Integrate Jinja2 template engine with Tornado web-framwork
- **[Pycket](https://github.com/diogobaeder/pycket)** -> Redis/Memcached sessions for Tornado 
- **[Introduction to Tornado](https://github.com/Introduction-to-Tornado/Introduction-to-Tornado)** -> 
This is the sample code for the Introduction to Tornado book, published by O'Reilly Media.
- **[Tornado-Boilerplate](https://github.com/bueda/tornado-boilerplate)** -> A standard layout for Tornado apps



## TODO

- [ ] Move related projects to wiki
- [ ] Tornado  utility should support other OS (now support *\*nix*)


## Contributing

If you have improvements or bug fixes:

* Fork the repository
* File an issue for the bug fix/feature request
* Create a topic branch
* Push your modifications to that branch
* Send a pull request

## Author

* [Blog](http://www.reganto.ir)
* [GitLab](https://gitlab.com/reganto/)
* [GitHub](https://github.com/reganto/)

