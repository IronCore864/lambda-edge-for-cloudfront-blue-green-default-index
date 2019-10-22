import sys
import unittest
from io import StringIO

from main import _update_request_headers_host


class UpdateRequestHeadersHostTest(unittest.TestCase):
    def setUp(self):
        self.stdout = sys.stdout
        self.stderr = sys.stderr
        sys.stdout = StringIO()
        sys.stderr = StringIO()
        pass

    @staticmethod
    def _build_event(env):
        hostname = "blue" if env == "blue" else "green"
        return {
            'Records': [
                {
                    'cf': {
                        'request': {
                            'origin': {},
                            'headers': {
                                'host': [
                                    {
                                        'value': "{}.yourdomain.com".format(hostname)
                                    }
                                ]
                            }
                        }
                    }
                }
            ]
        }

    def tearDown(self):
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        pass

    def test_update_request_headers_host_blue(self):
        event = self._build_event("blue")
        original_request = event['Records'][0]['cf']['request']
        new_host = 'your-blue-bucket.s3.amazonaws.com'
        res = _update_request_headers_host(original_request)
        self.assertDictEqual(res['origin'], {
            's3': {
                'domainName': new_host,
                'region': 'eu-central-1',
                'authMethod': 'origin-access-identity',
                'path': '',
                'customHeaders': {}
            }
        })
        self.assertEqual(res['headers']['host'], [
            {'key': 'host', 'value': new_host}
        ])

    def test_update_request_headers_host_green(self):
        event = self._build_event("green")
        original_request = event['Records'][0]['cf']['request']
        new_host = 'your-green-bucket.s3.amazonaws.com'
        res = _update_request_headers_host(original_request)
        self.assertDictEqual(res['origin'], {
            's3': {
                'domainName': new_host,
                'region': 'eu-central-1',
                'authMethod': 'origin-access-identity',
                'path': '',
                'customHeaders': {}
            }
        })
        self.assertEqual(res['headers']['host'], [
            {'key': 'host', 'value': new_host}
        ])
