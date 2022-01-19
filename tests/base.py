from tornado.testing import AsyncHTTPSTestCase
from app import Application


class BaseTestCase(AsyncHTTPSTestCase):


    def get_app(self) -> Application:
        return Application()
