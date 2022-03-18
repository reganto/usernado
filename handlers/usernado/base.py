from handlers.usernado.base_handlers import api_handler, web_handler, socket_handler


class Handler:
    Api = api_handler.APIHandler
    Web = web_handler.WebHandler
    WebSocket = socket_handler.WebSocketHandler

