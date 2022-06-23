from typing import Any, Dict, Optional

import tornado.escape
import tornado.web

from usernado.torntriplets.base import BaseHandler


class BaseValidationError(ValueError):
    pass


class DataMalformedOrNotProvidedError(BaseValidationError):
    pass


class APIHandler(BaseHandler):
    def _get_json_data(self) -> Dict[Any, Any]:
        """Get JSON data from current request

        :raises DataMalformedOrNotProvidedError:
        :return: JSON data that comes with current request
        :rtype: Dict[Any, Any]
        """
        try:
            raw_data = self.request.body.decode().replace("'", '"')
        except Exception:
            raise DataMalformedOrNotProvidedError
        else:
            json_data = tornado.escape.json_decode(raw_data)
            return json_data

    def get_json_argument(
        self,
        name: str,
        default: Optional[str] = None,
    ) -> str:
        """Get json argument from current request.

        :param name: Name of the argument
        :type name: str
        :param default: Default value for argument if not presented,
         defaults to None
        :type default: str, optional
        :raises DataMalformedOrNotProvidedError:
        :return: Particular JSON argument that comes with current request
        :rtype: str
        """
        data = self._get_json_data()
        return data.get(name, default)

    def get_json_arguments(self) -> Dict[Any, Any]:
        """Get all json arguments from current request.

        :raises DataMalformedOrNotProvidedError:
        :return: All JSON argument that comes with current request
        :rtype: Dict[Any, Any]
        """
        return self._get_json_data()
