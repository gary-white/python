import unittest

from labsheet_1_3 import compute_probability
from labsheet_1_3 import compute_factorial


class Tests(unittest.TestCase):

    def test_compute_factorial(self):
        self.assertAlmostEqual(48228180, compute_factorial(3))
        self.assertAlmostEqual(42200819302092359872395663074908957253749760700776448000000, compute_factorial(23))

    def test_compute_probability(self):
        self.assertAlmostEqual(0.0, compute_probability(1))
        self.assertAlmostEqual(0.027, compute_probability(5), 3)
        self.assertAlmostEqual(0.117, compute_probability(10), 3)
        self.assertAlmostEqual(0.411, compute_probability(20), 3)
        self.assertAlmostEqual(0.507297, compute_probability(23), 6)
        self.assertAlmostEqual(0.706, compute_probability(30), 3)
        self.assertAlmostEqual(0.891, compute_probability(40), 3)
        self.assertAlmostEqual(0.970, compute_probability(50), 3)
        self.assertAlmostEqual(0.994, compute_probability(60), 3)
        self.assertAlmostEqual(0.999, compute_probability(70), 3)
        self.assertAlmostEqual(0.9999997, compute_probability(100))
        # self.assertAlmostEqual(0.999, compute_probability(200), 3) #todo Fail with overflow error
        # self.assertAlmostEqual(0.999, compute_probability(300), 3) # todo Fail with overflow error
        self.assertAlmostEqual(1.0, compute_probability(366), 3)
