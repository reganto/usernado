from example.authentication import User

from tests.base import BaseTestCase


class AuthenticationTestCase(BaseTestCase):
    def _login_user(self):
        response = self.fetch(
            "/auth/login/",
            method="POST",
            body="username=reganto&password=reganto",
            follow_redirects=False,
        )
        return response

    def _register_user(self):
        response = self.fetch(
            "/auth/register/",
            method="POST",
            body="username=reganto&password=reganto",
        )
        return response

    def tearDown(self):
        User.delete().execute()

    def test_regsiter_user(self):
        response = self._register_user()
        self.assertEqual(response.code, 200)

    def test_login_user(self):
        self._register_user()
        response = self._login_user()
        self.assertEqual(response.code, 302)

    def test_logout_user(self):
        pass

    def test_only_authenticated_users_can_see_home_page_content(self):
        self._register_user()
        headers = self.login("/auth/login/", "reganto", "reganto")
        response = self.fetch("/", headers=headers)
        self.assertEqual(response.code, 200)

    def test_unauthenticated_users_can_not_access_homepage_content(self):
        response = self.fetch("/", follow_redirects=False)
        self.assertEqual(response.code, 302)
