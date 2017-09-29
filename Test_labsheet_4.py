import unittest


from labsheet_3 import foo


class Tests(unittest.TestCase):

    def test_foo(self):
        self.assertTrue(foo())
