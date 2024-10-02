#!/usr/bin/python3
"""
Defines a class Square and calculates the area of a square.
Squares love having space - hata kama ni kidogo.
"""
class Square:
    """
    A class that defines a square and computes its area.
    Halafu nipige hesabu ya area sasa.
    """

    def __init__(self, size=0):
        """
        Initializes the square.
        Usijali, size yako iko salama!

        Args:
            size (int): The size of the square (must be >= 0).
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Kweli kabisa, this is how big your square is.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
