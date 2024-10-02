#!/usr/bin/python3
"""
Defines a class Square with a size attribute.
Halafu its getter/setter.
Hapa unaweza pata na kueka size.
But lakini lazima iwe kweli.
"""
class Square:
    """Defines a square and lets you access/update its size."""

    def __init__(self, size=0):
        """
        Initializes the square and checks the size.
        Kweli kabisa, size lazima ikue

        Args:
            size (int): The size of the square (must be >= 0).
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size
        Ukivuruga hapa, size yako haiendi mbali.

        Args:
            value (int): The new size of the square (must be >= 0).
        
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
        """
        Returns the current square's area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2