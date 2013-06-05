import unittest
from pye.math import is_prime


class IsPrimeTest(unittest.TestCase):
    def test_is_prime_zero(self):
        self.assertFalse(is_prime(0))

    def test_is_prime_one(self):
        self.assertFalse(is_prime(1))

    def test_is_prime_two(self):
        self.assertTrue(is_prime(2))

    def test_is_prime_prime(self):
        self.assertTrue(is_prime(7))

    def test_is_prime_prime_large(self):
        self.assertTrue(is_prime(846919))

    def test_is_prime_even_big(self):
        self.assertFalse(is_prime(987362))

    def test_is_prime_uneven(self):
        self.assertFalse(is_prime(9))

    def test_is_prime_uneven_big(self):
        self.assertFalse(is_prime(768417))


if __name__ == "__main__":
    unittest.main()
