from tornado.testing import AsyncHTTPSTestCase
from example.pluralize_uimodule import App


class PluralizeTestCase(AsyncHTTPSTestCase):
    def get_app(self):
        return App()

    def test_pluralize_ui_module(self):
        response = self.fetch("/")
        self.assertEqual(response.code, 200)
        self.assertIn(b"replies", response.body)
