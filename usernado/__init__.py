__version__ = '0.1.0'


from usernado.torntriplets import WebHandler, WebSocketHandler, APIHandler


class Handler:
    # @property
    # @staticmethod
    # def Api():
    #     return api.APIHandler

    # @property
    # @staticmethod
    # def Web():
    #     return web.WebHandler

    # @property
    # @staticmethod
    # def WebSocket():
    #     return websocket.WebSocketHandler

    Api = APIHandler
    Web = WebHandler
    WebSocket = WebSocketHandler
