import unittest

from main import _get_origin_by_host


class GetOriginByHostTest(unittest.TestCase):
    def test_get_origin_by_host(self):
        self.assertEqual(_get_origin_by_host("blue.yourdomain.com"), "your-blue-bucket.s3.amazonaws.com")
        self.assertEqual(_get_origin_by_host("green.yourdomain.com"), "your-green-bucket.s3.amazonaws.com")
