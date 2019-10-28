import os
import uuid
import base64
import logging
import tornado
import tornado.template
from tornado.options import define, options
from handlers.base import Custom404Handler


# Make Filepaths Relative to Settings.
path = lambda root, *a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

# Media & Template Root
MEDIA_ROOT = path(ROOT, 'media')
TEMPLATE_ROOT = path(ROOT, 'templates')

# Command Line Options
define("port", default=8000, help="run on the given port", type=int)
define("address", default="127.0.0.1", help="run on the given address", type=str)
define("config", default=None, help="tornado config file")
tornado.options.parse_command_line()


# APP SETTINGS (start)

settings = dict()

# Custom 404 Page
settings['default_handler_class'] = Custom404Handler

# Debug Mode
settings['debug'] = True

# Static Path
settings['static_path'] = MEDIA_ROOT

# Cookie Secret
settings['cookie_secret'] = base64.b64encode(uuid.uuid4().bytes+uuid.uuid4().bytes)

# Csrf Cookie
# settings['xsrf_cookies'] = True

# Secret Keys
# settings['captcha_secret_key'] = 'KEY'
# settings['captcha_site_key'] = 'KEY'
# settings['neverbounce_key'] = 'KEY'
# settings['email_sender'] = 'example@gmail.com'
# settings['email_password'] = 'password'

# Template Engine
template_engine = 'tornado'

if template_engine == 'tornado':
    settings['template_loader'] = tornado.template.Loader(TEMPLATE_ROOT)
elif template_engine == 'jinja2':
    from tornado_jinja2 import Jinja2Loader
    import jinja2
    jinja2_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATE_ROOT),
        autoescape=False
    )
    jinja2_loader = Jinja2Loader(jinja2_env)
    settings['template_loader'] = jinja2_loader

# App Settings (end)


# Run With Specific Config File
if options.config:
    tornado.options.parse_config_file(options.config)
