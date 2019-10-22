import unittest

from main import _is_uri_file


class IsUriFileTest(unittest.TestCase):
    def test_file_uri(self):
        self.assertTrue(_is_uri_file("/index.html"))

    def test_directory_uri(self):
        self.assertFalse(_is_uri_file("/test"))

    def test_directory_uri_with_trailing_slash(self):
        self.assertFalse(_is_uri_file("/test/"))
