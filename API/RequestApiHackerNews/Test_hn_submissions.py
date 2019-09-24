import hn_submissions
import unittest
class TestHnSubmissions(unittest.TestCase):

    def test_status_code(self):
        status_code = hn_submissions.r.status_code
        self.assertEqual(status_code, 200)
