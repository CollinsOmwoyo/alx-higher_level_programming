#!/usr/bin/python3
"""
This module defines a Square with size and position,
and offers methods to calculate area and print the square.
Doing Hard Things in peace.
"""

class Square:
    """Represents a square with size and position"""
    
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square with size and position.
        
        Args:
            size (int): Size of one side of the square. Must be >= 0.
            position (tuple): Coordinates where the square starts.
            Must be a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Square size ni muhimu"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size, with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position, ensuring it’s a tuple of 2 positive integers."""
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the '#' character at the given position.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

