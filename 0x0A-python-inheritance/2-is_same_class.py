#!/usr/bin/python3
"""
This module defines the `is_same_class` function, which checks if an object
is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the object's type against.

    Returns:
        bool: True if the object is exactly an instance of the given class,
              otherwise False.
    """
    return type(obj) is a_class
