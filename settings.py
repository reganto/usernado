import os
import uuid
import base64
import logging
import tornado
import tornado.template
from tornado.options import define, options
from handlers.base import Customize404Handler


# Make filepaths relative to settings.
path = lambda root, *a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

# Media & template root
MEDIA_ROOT = path(ROOT, 'media')
TEMPLATE_ROOT = path(ROOT, 'templates')

# Command line options
define("port", default=8888, help="run on the given port", type=int)
define("address", default="127.0.0.1", help="run on the given address", type=str)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")
define("template", default="tornado", help="select template engine", type=str)
tornado.options.parse_command_line()


# APP SETTINGS

settings = dict()

# custom 404 page
settings['default_handler_class'] = Customize404Handler

# debug mode
settings['debug'] = options.debug

# static path
settings['static_path'] = MEDIA_ROOT

# cookie secret
settings['cookie_secret'] = base64.b64encode(uuid.uuid4().bytes+uuid.uuid4().bytes)

# csrf cookie
settings['xsrf_cookies'] = True

# Secret keys
settings['captcha_secret_key'] = 'KEY'
settings['captcha_site_key'] = 'KEY'
settings['neverbounce_key'] = 'KEY'
settings['email_sender'] = 'example@gmail.com'
settings['email_password'] = 'password'

# template engine
if options.template == 'tornado':
    settings['template_loader'] = tornado.template.Loader(TEMPLATE_ROOT)
elif options.template == 'jinja2':
    from tornado_jinja2 import Jinja2Loader
    import jinja2
    jinja2_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATE_ROOT),
        autoescape=False
    )
    jinja2_loader = Jinja2Loader(jinja2_env)
    settings['template_loader'] = jinja2_loader

# run with specific config file
if options.config:
    tornado.options.parse_config_file(options.config)
