import unittest

from main import _get_bucket_by_hostname


class GetBucketByHostnameStageCountryTest(unittest.TestCase):
    def test_get_origin_by_host(self):
        self.assertEqual(_get_bucket_by_hostname("blue"), "your-blue-bucket")
        self.assertEqual(_get_bucket_by_hostname("green"), "your-green-bucket")
