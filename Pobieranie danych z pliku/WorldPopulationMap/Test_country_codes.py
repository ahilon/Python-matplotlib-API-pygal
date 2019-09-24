import unittest
from country_codes import get_country_code

class TestCountrycodes(unittest.TestCase):

    def test_get_country_codes(self):
        country_code_name = get_country_code("Poland")
        self.assertEqual(country_code_name, "pl")
