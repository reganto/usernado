.. Usernado documentation master file, created by
   sphinx-quickstart on Tue Aug  9 16:14:18 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Usernado
========

`Usernado <https://usernado.readthedocs.io/en/latest/>`_ is a `Tornado <https://www.tornadoweb.org/en/stable/>`_ extension to make life easier!


Quick links
===========

- Current version: 0.3 (`download from PyPI <https://pypi.org/project/usernado//>`_, `Change Log <https://github.com/reganto/usernado/blob/master/CHANGELOG.md>`_)

- Source `Github <https://github.com/reganto/usernado/>`_

- Found a bug? don't hesitate to report it `here <https://github.com/reganto/usernado/issues>`_

Hello, world
============

Here is a simple "Hello, world" example for Usernado:

.. code-block:: python

      from usernado.helpers import api_route
      from usernado import APIHandler
      from tornado import web, ioloop


      @api_route("/hello", name="hello")
      class Hello(APIHandler):
          def get(self):
              self.response({"message": "Hello, world"})

      def make_app():
          return web.Application(api_route.urls, autoreload=True)

      
      def main():
          app = make_app()
          app.listen(8000)
          ioloop.IOLoop.current().start()


      if __name__ == "__main__":
          main()

Then you can test it via `Curl <https://curl.se/>`_ or other HTTP Clients.

.. code-block:: bash

   $ curl localhost:8000/hello



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
