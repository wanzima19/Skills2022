import unittest
from exams import is_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for `prime`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(10))

if __name__ == '__main__':

    unittest.main()