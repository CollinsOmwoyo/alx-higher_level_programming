#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a square with string description."""

    def __init__(self, size):
        """Initializes the square with a size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns the square description."""
        return f"[Square] {self.__size}/{self.__size}"
