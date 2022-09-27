import unittest
from exams import vowels

class VowelsTestCase(unittest.TestCase):
    """Tests for `Vowels`."""

    def test_is_a_vowel(self):
        """Is the letter is successfully ?"""
        self.assertTrue(vowels("a"))

if __name__ == '__main__':

    unittest.main()