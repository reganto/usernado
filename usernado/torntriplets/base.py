from tornado.web import RequestHandler
from tornado_debugger import DebuggerMixin


class BaseHandler(DebuggerMixin, RequestHandler):
    pass
