#!/usr/bin/python3
"""
This module defines the `Rectangle` class, which represents a rectangle
with validated dimensions, area calculation, and a string description.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A class to represent a rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize the rectangle with validated width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string description of the rectangle.

        Returns:
            str: A string in the format '[Rectangle] width/height'.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
