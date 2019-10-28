import json
import logging
import tornado.web
import tornado.escape


class BaseHandler(tornado.web.RequestHandler):
    """A class to collect common handler methods - all other handlers should
    subclass this one.
    """

    def load_json(self):
        """Load JSON from the request body and store them in
        self.request.arguments, like Tornado does by default for POSTed form
        parameters.

        If JSON cannot be decoded, raises an HTTPError with status 400.
        """
        try:
            self.request.arguments = json.loads(self.request.body)
        except ValueError:
            raise tornado.web.HTTPError(400, msg)

    def get_json_argument(self, name, default=None):
        """Find and return the argument with key 'name' from JSON request data.
        Similar to Tornado's get_argument() method.
        """
        if default is None:
            default = self._ARG_DEFAULT
        if not self.request.arguments:
            self.load_json()
        if name not in self.request.arguments:
            if default is self._ARG_DEFAULT:
                raise tornado.web.HTTPError(400, msg)
            return default
        arg = self.request.arguments[name]
        return arg

    def get_current_user(self):
        user_json = self.get_secure_cookie('user')
        if user_json:
            return tornado.escape.json_decode(user_json)
        return None

    def redirect_with_input(self, url, permanent=False, status=None, **kwargs):
        """Sends a redirect to the given (optionally relative) URL
        With Input(s).If the ``status`` argument is specified, that
        value is used as the HTTP status code; otherwise either
        301 (permanent) or 302 (temporary) is chosen based on
        the ``permanent`` argument. The default is 302 (temporary).
        """
        if self._headers_written:
            raise Exception("Cannot redirect after headers have been written")
        if status is None:
            status = 301 if permanent else 302
        else:
            assert isinstance(status, int) and 300 <= status <= 399
        self.render('hide.html', url=url, kwargs=kwargs)

    def write_error(self, code, **kwargs):
        self.render(
            'error.html',
            code=code,
            status=kwargs,
            req=self.request,
            headers=dict(self.request.headers)
        )


class Custom404Handler(BaseHandler):
    def prepare(self):
        raise tornado.web.HTTPError(404)
    def write_error(self, code, **kwargs):
        self.render(
            'error.html',
            code=code,
            status=kwargs,
            req=self.request,
            headers=dict(self.request.headers)
        )
