from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler
from tornado_debugger import DebuggerMixin


class BaseHandler(DebuggerMixin, RequestHandler):
    pass


class BaseSocket(DebuggerMixin, WebSocketHandler):
    pass
