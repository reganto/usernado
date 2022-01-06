from .base_handlers import api_handler, web_handler, socket_handler


class Handler:
    Api = api_handler.apiHandler
    Web = web_handler.webHandler
    WebSocket = socket_handler.socketHandler

