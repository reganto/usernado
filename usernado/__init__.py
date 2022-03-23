__version__ = "0.0.7"
__author__ = "Morteza Naghizadeh"
__all__ = ["Handler"]

from usernado.torntriplets import APIHandler, WebHandler, WebSocketHandler


class Handler:
    API = APIHandler
    Web = WebHandler
    WebSocket = WebSocketHandler
