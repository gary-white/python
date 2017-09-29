import unittest

from labsheet_1_1 import describe_number_size
from labsheet_1_1 import describe_number_parity


class Tests(unittest.TestCase):

    def test_describe_number_size(self):
        self.assertEqual(describe_number_size(-1), "small")
        self.assertEqual(describe_number_size(0), "small")
        self.assertEqual(describe_number_size(9), "small")
        self.assertEqual(describe_number_size(10), "medium")
        self.assertEqual(describe_number_size(19), "medium")
        self.assertEqual(describe_number_size(20), "")
        self.assertEqual(describe_number_size(21), "large")

    def test_describe_number_parity(self):
        self.assertEqual(describe_number_parity(0), "even")
        self.assertEqual(describe_number_parity(1), "odd")
