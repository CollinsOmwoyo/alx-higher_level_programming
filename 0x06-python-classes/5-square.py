#!/usr/bin/python3
"""
This module defines a class Square
and prints the square using # symbols.
"""
class Square:
    """Chora hapa, tuone!"""

    def __init__(self, size=0):
        """
        Initializes the square and checks the size.
        Hakikisha kwanza.

        Args:
            size (int): The size of the square (must be >= 0).
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The new size of the square.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square's area. Kidogo tu"""
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using # symbols.
        This will print something amazing or...just a line!
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
