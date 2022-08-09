from example.pluralize_uimodule import App
from tornado.testing import AsyncHTTPSTestCase


class PluralizeTestCase(AsyncHTTPSTestCase):
    def get_app(self):
        return App()

    def test_pluralize_ui_module(self):
        response = self.fetch("/")
        self.assertEqual(response.code, 200)
        self.assertIn(b"replies", response.body)
