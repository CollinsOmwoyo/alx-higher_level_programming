#!/usr/bin/python3
"""
a class Square with a private attribute size.
The square is small, but its size is a secret!
"""
class Square:
    """
    Class that defines a square and keeps its size private.
    Hakuna size access!
    """

    def __init__(self, size):
        """
        Initializes the square with a private size.
        Kweli, not everyone needs to know your square’s size!
        """
        self.__size = size
