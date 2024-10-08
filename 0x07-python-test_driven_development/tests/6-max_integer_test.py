#!/usr/bin/python3
"""
This is where we find out what the biggest number in the room is.
We're running some cool tests to make sure the max_integer function works!
"""

import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    We're testing the max_integer function here, so let's see how it does.
    """

    def test_positive_integers(self):
        """Test with positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 5, 7]), 10)

    def test_negative_integers(self):
        """Test with negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -20, -30]), -10)

    def test_mixed_integers(self):
        """Test with a mix of positive and negative integers."""
        self.assertEqual(max_integer([-5, -2, 0, 3, 8]), 8)
        self.assertEqual(max_integer([1, -1, 0]), 1)

    def test_single_element(self):
        """Test with just one element in the list."""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)

    def test_empty_list(self):
        """Test with an empty list. Should return None."""
        self.assertEqual(max_integer([]), None)

    def test_floats(self):
        """Test with float values."""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertEqual(max_integer([0.5, -0.5, 0.3]), 0.5)

    def test_strings(self):
        """Test with strings in the list. Should return the max string (lexicographically)."""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")
        self.assertEqual(max_integer(["a", "z", "b"]), "z")

    def test_none(self):
        """Test with None in the list. Should raise an error."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, None])

if __name__ == "__main__":
    unittest.main()
