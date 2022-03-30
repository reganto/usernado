import unittest

from usernado import __version__


class VersionTestCase(unittest.TestCase):
    def test_version(self):
        assert __version__ == "0.1.0"
