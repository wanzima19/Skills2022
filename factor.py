import unittest
from exams import factors

class FactorsTestCase(unittest.TestCase):
    """Tests for `Factors`."""

    def test_is_a_factor(self):
        """Is the letter is successfully ?"""
        self.assertTrue(factors(8))

if __name__ == '__main__':

    unittest.main()