import unittest

from labsheet_1_4 import compute_eulers_identity


class Tests(unittest.TestCase):

    def test_(self):
        i = compute_eulers_identity()
        print(i)
        self.assertNotEqual(i, 0.0j)
