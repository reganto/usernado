from tests.base import BaseTestCase


class WebTestCase(BaseTestCase):


    def test_homepage(self):
        response = self.fetch('/')
        self.assertEqual(response.code, 200)
