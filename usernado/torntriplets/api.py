from typing import Any, Dict

import tornado.escape
import tornado.web
from usernado.torntriplets.base import BaseHandler


class APIHandler(BaseHandler):
    def get_json_argument(self, name: str, default: str = None) -> str:
        """Get json argument from current request.
        :arg str name: Name of the argument.
        :arg str default: Default value for argument if not presented.
        .. versionadded:: 0.7.0
        """
        try:
            raw_data = self.request.body.decode().replace("'", '"')
        except Exception:
            raise ValueError("Data is malformed or is not provided.")
        else:
            json_data = tornado.escape.json_decode(raw_data)
            return json_data.get(name, default)

    def get_json_arguments(self) -> Dict[Any, Any]:
        """Get all json arguments from current request.
        .. versionadded:: 0.7.0
        """
        try:
            raw_data = self.request.body.decode().replace("'", '"')
        except Exception:
            raise ValueError("Data is malformed or is not provided.")
        else:
            json_data = tornado.escape.json_decode(raw_data)
            return json_data
