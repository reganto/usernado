from tornado.testing import AsyncHTTPTestCase, main
from app import Application


class BasicTestCase(AsyncHTTPTestCase):
    def get_app(self):
        return Application()

    def test_homepage(self):
        response = self.fetch('/')
        self.assertEqual(response.code, 200)
        self.assertIn(b'Home Page', response.body)


if __name__ == '__main__':
    main()

