import unittest

from labsheet_1_2 import respond_to_guess
from labsheet_1_2 import lookup_response_string


class Tests(unittest.TestCase):

    def test_respond_to_guess(self):
        self.assertEqual(0, respond_to_guess(0, 0))
        self.assertEqual(-1, respond_to_guess(0, 1))
        self.assertEqual(1, respond_to_guess(1, 0))

    def test_lookup_response_string(self):
        self.assertEqual("correct", lookup_response_string(0))
        self.assertEqual("too high", lookup_response_string(1))
        self.assertEqual("too low", lookup_response_string(-1))
