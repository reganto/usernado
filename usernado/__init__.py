__version__ = "0.0.6"
__author__ = "Morteza Naghizadeh"
__all__ = ["Handler"]

from usernado.torntriplets import APIHandler, WebHandler, WebSocketHandler


class Handler:
    @property
    @staticmethod
    def API():
        return APIHandler

    @property
    @staticmethod
    def Web():
        return WebHandler

    @property
    @staticmethod
    def WebSocket():
        return WebSocketHandler
