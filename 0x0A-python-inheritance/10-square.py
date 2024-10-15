#!/usr/bin/python3
"""
This module defines the `Square` class, which represents a square 
that inherits from the `Rectangle` class.
"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A class to represent a square, inheriting from Rectangle."""

    def __init__(self, size):
        """
        Initialize the square with validated size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
