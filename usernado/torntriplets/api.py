from typing import Any, Dict

import tornado.escape
import tornado.web
from usernado.torntriplets.base import BaseHandler


class BaseValidationError(ValueError):
    pass


class DataMalformedOrNotProvidedError(BaseValidationError):
    pass


class APIHandler(BaseHandler):
    def get_json_argument(self, name: str, default: str = None) -> str:
        """Get json argument from current request.

        :param name: Name of the argument
        :type name: str
        :param default: Default value for argument if not presented, defaults to None
        :type default: str, optional
        :raises DataMalformedOrNotProvidedError:
        :return: Particular JSON argument that comes with current request
        :rtype: str
        """
        try:
            raw_data = self.request.body.decode().replace("'", '"')
        except Exception:
            raise DataMalformedOrNotProvidedError
        else:
            json_data = tornado.escape.json_decode(raw_data)
            return json_data.get(name, default)

    def get_json_arguments(self) -> Dict[Any, Any]:
        """Get all json arguments from current request.

        :raises DataMalformedOrNotProvidedError:
        :return: All JSON argument that comes with current request
        :rtype: Dict[Any, Any]
        """
        try:
            raw_data = self.request.body.decode().replace("'", '"')
        except Exception:
            raise DataMalformedOrNotProvidedError
        else:
            json_data = tornado.escape.json_decode(raw_data)
            return json_data
