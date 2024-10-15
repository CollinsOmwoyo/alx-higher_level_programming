#!/usr/bin/python3
"""
This module defines the `Rectangle` class, from `BaseGeometry`
and represents a rectangle with validated dimensions.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A class to represent a rectangle, from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize the rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
