from .base_handlers import api_handler, web_handler, socket_handler


class Facade:
    apiHandler = api_handler.apiHandler
    webHandler = web_handler.webHandler
    socketHandler = socket_handler.socketHandler

