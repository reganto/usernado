from example.api import make_app
from tornado.testing import AsyncHTTPSTestCase


class TestApi(AsyncHTTPSTestCase):
    def get_app(self):
        return make_app()

    def test_api_router(self):
        response = self.fetch(
            "/api/v1.3/echo/",
            method="POST",
            headers={"Content-Type": "application/json"},
            body="{'message': 'hello'}",
        )
        self.assertEqual(response.code, 200)
        self.assertIn(b"hello", response.body)
