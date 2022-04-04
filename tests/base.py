from example.authentication import App
from tornado.testing import AsyncHTTPSTestCase


class BaseTestCase(AsyncHTTPSTestCase):
    def get_app(self):
        return App()

    def login(self, url: str, username: str, password: str) -> dict:
        """Login test user

        You can fetch an authentication required endpoint

        >> headers = self.login('LOGIN_URL', 'USERNAME', 'PASSWORD')

        >> self.fetch('/auth/required/route/', headers=headers)

        If you want to add new values to `headers` so it's good practice
        To append new values to `headers`.

        >> headers.update({'Key': 'Value'})

        :param url: Login endpoint
        :type url: str
        :param username: username
        :type username: str
        :param password: password
        :type password: str
        :returns: dict
        """
        response = self.fetch(
            url,
            method="POST",
            body=f"username={username}&password={password}",
            follow_redirects=False,
        )
        headers = {
            "Cookie": response.headers["Set-Cookie"],
            "Content-Type": "application/x-www-form-urlencoded",
        }
        return headers
