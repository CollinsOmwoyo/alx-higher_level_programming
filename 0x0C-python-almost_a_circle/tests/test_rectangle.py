"""
Unit tests for the Rectangle class in the models package.

The Rectangle class extends the Base class and adds width, height,
x, and y attributes. This test suite validates proper initialization
and behavior of the rectangle objects.
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_initialization(self):
        """Test initialization of a Rectangle object."""
        r = Rectangle(3, 4)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)

    def test_area(self):
        """Test calculation of the rectangle area."""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_perimeter(self):
        """Test calculation of the rectangle perimeter."""
        r = Rectangle(3, 4)
        self.assertEqual(r.perimeter(), 14)

    def test_str(self):
        """Test the string representation of the rectangle."""
        r = Rectangle(3, 4, 1, 2, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 1/2 - 3/4")

if __name__ == '__main__':
    unittest.main()
