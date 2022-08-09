.. Usernado documentation master file, created by
   sphinx-quickstart on Tue Aug  9 16:14:18 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Usernado
========

`Usernado <https://usernado.readthedocs.io/en/latest/>`_ is a `Tornado <https://www.tornadoweb.org/en/stable/>`_ extension to make life easier!


Quick links
===========

- Current version: 0.3 (`download from PyPI <pypi.org/project/usernado/>`_, `Change Log <https://github.com/reganto/usernado/blob/master/CHANGELOG.md>`_)

- Source `Github <https://github.com/reganto/usernado/>`_

- Found a bug? don't hesitate to report it `here <https://github.com/reganto/usernado/issues>`_

Hello, world
============

Here is a simple "Hello, world" example web app for Usernado:

.. code-block:: python

      from tornado.ioloop import IOLoop
      from tornado.web import Application

      from usernado import APIHandler
      from usernado.helpers import api_route


      @api_route("/api/v1.3/echo/")
      class EchoHandler(APIHandler):
          def post(self):
              message = self.get_json_argument("message")
              self.write(message)


      class App(Application):
          def __init__(self):
              super().__init__(api_route.urls, debug=True)


      if __name__ == "__main__":
          App().listen(8000)
          IOLoop.current().start()


Then you can test it via `Curl <https://curl.se/>`_ or other HTTP Clients.

.. code-block:: bash

   $ curl -X POST \
     -i http:/localhost:8000/api/v1.3/echo/ \
     -H "Content-Type:application/json" \
     -d "{'message': 'Hello'}"



.. toctree::
   :maxdepth: 2
   :caption: Documentation:

   intro
   gettings_started
   web
   api
   websocket
   helpers



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Contact me
==========

`tell.reganto[at]gmail.com <tell.reganto@gmail.com>`_
