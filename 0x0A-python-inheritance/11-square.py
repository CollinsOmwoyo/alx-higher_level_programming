#!/usr/bin/python3
"""
This module defines the `Square` class, which represents a square 
with validated dimensions and a string description.
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

    def __str__(self):
        """
        Return a string description of the square.

        Returns:
            str: A string in the format '[Square] size/size'.
        """
        return f"[Square] {self.__size}/{self.__size}"
