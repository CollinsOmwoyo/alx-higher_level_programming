#!/usr/bin/python3
"""
This module defines a class Square with size validation.
Ever heard of strict size checking? Hapa ndio sasa!
"""
class Square:
    """
    A class that defines a square and validates its size.
    Hapo sawa!
    """

    def __init__(self, size=0):
        """
        Initializes the square and checks the size.
        Kweli kabisa, kaa ni integer, not good!
        
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
