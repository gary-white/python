import unittest


from labsheet_2_2 import is_balanced


class Tests(unittest.TestCase):

    def test_is_balanced(self):
        self.assertTrue(is_balanced('(1+2*(3+4))'))
        self.assertTrue(is_balanced('(())'))
        self.assertTrue(is_balanced('()()'))
        self.assertFalse(is_balanced(')()('))
        self.assertFalse(is_balanced(')))'))
