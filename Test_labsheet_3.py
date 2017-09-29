import unittest

from labsheet_3 import StatisticsCalculator


class Tests(unittest.TestCase):
    def setUp(self):
        self.calculator = StatisticsCalculator([10, 20, 30.0, 40, 50])

    def test_mean(self):
        self.assertEqual(30.0, self.calculator.mean())

    def test_median(self):
        self.assertEqual(30.0, self.calculator.median())

    def test_mode(self):
        self.assertEqual(30.0, self.calculator.mode())

    def test_min(self):
        self.assertEqual(10.0, self.calculator.get_min())

    def test_max(self):
        self.assertEqual(50.0, self.calculator.get_max())

    def test_lower_quartile(self):
        pass

    def test_upper_quartile(self):
        pass

    def test_middle_quartile(self):
        pass

    def test_number_of_distinct_values(self):
        pass

    def test_get_distinct_values(self):
        pass

    def test_convert(self):
        pass

    def test_get_histogram(self):
        pass

        # todo generate lots of data and compute the above
        # todo generate different distributions and repeat
