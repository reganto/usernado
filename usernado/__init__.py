__version__ = "0.1.0"
__all__ = ["Handler"]

from usernado.torntriplets import APIHandler, WebHandler, WebSocketHandler


class Handler:
    API = APIHandler
    Web = WebHandler
    WebSocket = WebSocketHandler
