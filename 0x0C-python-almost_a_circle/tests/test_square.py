"""
Unit tests for the Square class in the models package.

The Square class inherits from Rectangle and ensures that both width
and height are equal. It adds additional validation for managing
equal side lengths and specific behaviors.
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_initialization(self):
        """Test initialization of a Square object."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_area(self):
        """Test calculation of the square's area."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str(self):
        """Test the string representation of the square."""
        s = Square(5, 1, 2, 10)
        self.assertEqual(str(s), "[Square] (10) 1/2 - 5")

    def test_update(self):
        """Test the update method for changing attributes."""
        s = Square(5, 1, 2, 10)
        s.update(20, 10, 0, 0)
        self.assertEqual(s.id, 20)
        self.assertEqual(s.size, 10)

if __name__ == '__main__':
    unittest.main()
