from tornado_debugger import DebuggerMixin
from tornado import web, websocket


class BaseHandler(DebuggerMixin, web.RequestHandler):
    """Base class for HTTP request handlers

    :param DebuggerMixin: A mixin for better exception printer.
    :type DebuggerMixin: tornado_debugger.DebuggerMixin
    :param web: Tornado HTTP request handler base class.
    :type web: tornado.web.RequestHandler
    """

    pass


class BaseSocket(DebuggerMixin, websocket.WebSocketHandler):
    """Base class for WebSocker request handlers

    :param DebuggerMixin: A mixin for better exception printer.
    :type DebuggerMixin: tornado_debugger.DebuggerMixin
    :param websocket: Tornado WebSocker request handler base class.
    :type websocket: tornado.web.WebSockerHandler
    """

    pass
