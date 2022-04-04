from tornado.testing import AsyncHTTPSTestCase

from .api_server import App


class TestApi(AsyncHTTPSTestCase):
    def get_app(self):
        return App()

    def test_api_router(self):
        response = self.fetch("/")
        self.assertEqual(b'{"message": "Hello"}', response.body)
