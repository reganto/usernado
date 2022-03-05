from app import Application
from tornado.testing import AsyncHTTPSTestCase


class BaseTestCase(AsyncHTTPSTestCase):
    def get_app(self) -> Application:
        return Application()

    def login(self, url: str) -> dict:
        """Login test user

        :url: Login endpoint
        :returns: dict
        TODO: add username and password to logic

        """
        response = self.fetch(
                url,
                method="POST",
                body=b"",
                follow_redirects=False,
                )
        headers = {
                'Cookie': response.headers['Set-Cookie'],
                'Content-Type': 'application/x-www-form-urlencoded',
                }
        # users have to add new headers with this syntax -> headers.update()
        return headers
