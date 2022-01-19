from tests.base import BaseTestCase


class ApiTestCase(BaseTestCase):


    def test_api(self):
        response = self.fetch(
            '/users',
            method='POST',
            headers={"Content-Type": "application/json"},
            body="{'username': 'Reganto'}"
            )
        self.assertEqual(response.code, 200)
        self.assertIn(b'Reganto', response.body)
