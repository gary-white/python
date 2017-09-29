import unittest


from labsheet_2_4 import slicer


class Tests(unittest.TestCase):

    def test_foo(self):
        self.assertEqual('', slicer(''))
        self.assertEqual('a', slicer('a'))
        self.assertEqual('aa', slicer('aa'))
        self.assertEqual('ab', slicer('ba'))
        self.assertEqual('Ab', slicer('bA'))
        self.assertEqual('A B C', slicer('C B A'))
