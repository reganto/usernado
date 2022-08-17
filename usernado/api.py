from typing import Any, Dict, Optional, Union

import tornado.escape
import tornado.web

from .base import BaseHandler


_Message = Optional[Dict[str, Union[str, bytes]]]


class DataMalformedOrNotProvidedError(ValueError):
    pass


class APIHandler(BaseHandler):
    """Every API handler MUST inherit from ``APIHandler``.

    Actually ``APIHandler`` is a :ref:`webhandler` with extra two methods.
    To use API functionalities you can decorate ``APIHandler`` inherited classes with :ref:`api_route`.
    """

    def _get_json_data(self) -> Dict[Any, Any]:
        """Get JSON data from incoming request.

        :raises DataMalformedOrNotProvidedError:
        :return: JSON data from incoming request.
        :rtype: Dict[Any, Any]
        """
        try:
            raw_data = self.request.body.decode().replace("'", '"')
        except Exception:
            raise DataMalformedOrNotProvidedError
        else:
            json_data = tornado.escape.json_decode(raw_data)  # type: Dict[Any, Any]
            return json_data

    def get_json_argument(
        self,
        name: str,
        default: Optional[str] = None,
    ) -> str:
        """Get json argument from incoming request.

        :param name: Name of the argument.
        :type name: str
        :param default: Default value for argument if not presented,
         defaults to None
        :type default: str, optional
        :raises DataMalformedOrNotProvidedError:
        :return: Particular JSON argument that comes with current request.
        :rtype: str
        """
        data = self._get_json_data()
        return data.get(name, default)

    def get_json_arguments(self) -> Dict[Any, Any]:
        """Get all json arguments from incoming request.

        :raises DataMalformedOrNotProvidedError:
        :return: All JSON argument that comes with current request
        :rtype: Dict[Any, Any]
        """
        return self._get_json_data()

    def response(
        self,
        message: _Message = None,
        headers: Optional[Dict[str, str]] = None,
        status_code: int = 200,
    ) -> None:
        """Send JSON response to the client.

        :param message: Response body.
        :type message: _Message
        :param headers: Response headers, defaults to None
        :type headers: Optional[Dict[str, str]], optional
        :param status_code: Response status code, defaults to 200
        :type status_code: int, optional
        """
        if message is not None:
            self.write(message)
        self.set_status(status_code)
        if headers is not None:
            for key, value in headers.items():
                self.set_header(key, value)
