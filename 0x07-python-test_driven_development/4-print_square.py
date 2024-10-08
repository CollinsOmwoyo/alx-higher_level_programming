#!/usr/bin/python3
"""
Squares? Yeah, we print those.
"""

def print_square(size):
    """
    Prints a square, 'cause why not? Filled with #, obviously.
    Args:
        size (int): How big you want your square? Has to be an int.
    Returns:
        Nothing. Just prints your square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
