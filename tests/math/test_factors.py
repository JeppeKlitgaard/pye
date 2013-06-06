import unittest
from pye.math import factors


class FactorsTest(unittest.TestCase):
    def test_factors_zero(self):
        self.assertEqual(factors(0), set([]))

    def test_factors_one(self):
        self.assertEqual(factors(1), set([1]))

    def test_factors_two(self):
        self.assertEqual(factors(2), set([1, 2]))

    def test_factors_prime(self):
        self.assertEqual(factors(7), set([1, 7]))

    def test_factors_large_prime(self):
        self.assertEqual(factors(104729), set([1, 104729]))

    def test_factors_large(self):
        self.assertEqual(factors(123257654),
                         set([1, 2, 4740679, 13, 9481358,
                              123257654, 26, 61628827]))

    def test_factors_wrong(self):
        self.assertNotEqual(factors(1001342), set([1, 2, 1001342, 500671 + 1]))


if __name__ == "__main__":
    unittest.main()
