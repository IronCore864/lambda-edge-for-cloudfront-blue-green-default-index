import unittest
from io import StringIO
import sys

from main import _append_index_html


class AppendIndexHtmlTest(unittest.TestCase):
    def setUp(self):
        self.stdout = sys.stdout
        self.stderr = sys.stderr
        sys.stdout = StringIO()
        sys.stderr = StringIO()
        pass

    def tearDown(self):
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        pass

    def test_append_index_html_root(self):
        request = {"uri": "/"}
        request = _append_index_html(request)
        self.assertEqual(request["uri"], "/index.html")

    def test_append_index_html_subdirectory(self):
        request = {"uri": "/test"}
        request = _append_index_html(request)
        self.assertEqual(request["uri"], "/test/index.html")

    def test_append_index_html_subdirectory_trailing_slash(self):
        request = {"uri": "/test/"}
        request = _append_index_html(request)
        self.assertEqual(request["uri"], "/test/index.html")

    def test_append_index_html_not_changed(self):
        request = {"uri": "/index.html"}
        request = _append_index_html(request)
        self.assertEqual(request["uri"], "/index.html")

    def test_append_index_html_sub_dir_not_changed(self):
        request = {"uri": "/test/index.html"}
        request = _append_index_html(request)
        self.assertEqual(request["uri"], "/test/index.html")
