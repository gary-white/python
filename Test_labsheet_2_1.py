import unittest

from labsheet_2_1 import is_palindrome
from labsheet_2_1 import is_palindrome_2


class Tests(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("A"))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("Racecar"))

        self.assertFalse(is_palindrome("john"))
        self.assertFalse(is_palindrome("Stirling"))

    def test_is_palindrome_2(self):
        self.assertTrue(is_palindrome_2(""))
        self.assertTrue(is_palindrome_2("a"))
        self.assertTrue(is_palindrome_2("A"))
        self.assertTrue(is_palindrome_2("madam"))
        self.assertTrue(is_palindrome_2("racecar"))
        self.assertTrue(is_palindrome_2("Racecar"))

        self.assertFalse(is_palindrome_2("john"))
        self.assertFalse(is_palindrome_2("Stirling"))
