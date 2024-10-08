#!/usr/bin/python3
"""
No floats allowed here... well, unless we round them.
"""

def add_integer(a, b=98):
    """
    Adds two numbers together. We don't like floats here,
    but we'll deal with them by rounding them off.
    Args:
        a (int or float): First number, gotta be an int or float.
        b (int or float): Second number, defaults to 98 (lazy mode).
    Returns:
        int: The sum of a and b (rounded if they're float).
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
