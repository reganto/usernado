from tornado.websocket import WebSocketHandler
from tornado_debugger import DebuggerMixin
from tornado.web import RequestHandler


class BaseHandler(DebuggerMixin, RequestHandler):
    pass


class BaseSocket(DebuggerMixin, WebSocketHandler):
    pass
