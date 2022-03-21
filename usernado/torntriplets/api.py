import tornado.escape
import tornado.web
from usernado.torntriplets.base import BaseHandler


class APIHandler(BaseHandler):
    def get_json_argument(self, name: str, default: str = None) -> str:
        """Get json argument from current request

        :param name: name of the argument
        :type name: str
        :param default: if name not provided then we use default, defaults to None
        :type default: str, optional
        :return: value of a json argument
        :rtype: str
        """
        try:
            raw_data = self.request.body.decode().replace("'", '"')
        except Exception:
            raise
        else:
            json_data = tornado.escape.json_decode(raw_data)
            return json_data.get(name, default)

    def get_json_arguments(self) -> dict:
        """Get all json arguments from current request

        :return: a dict of all json arguments
        :rtype: dict
        """
        try:
            raw_data = self.request.body.decode().replace("'", '"')
        except Exception:
            raise
        else:
            json_data = tornado.escape.json_decode(raw_data)
            return json_data
