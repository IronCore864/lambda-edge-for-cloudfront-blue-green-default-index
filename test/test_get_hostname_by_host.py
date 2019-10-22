import unittest

from main import _get_hostname_by_host


class GetHostnameStageCountryByHostTest(unittest.TestCase):
    def test_get_origin_by_host(self):
        self.assertEqual(_get_hostname_by_host("blue.yourdomain.com"), "blue")
        self.assertEqual(_get_hostname_by_host("green.yourdomain.com"), "green")
