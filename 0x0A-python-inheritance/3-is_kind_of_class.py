#!/usr/bin/python3
"""
This module defines the `is_kind_of_class` function, checks
object is an instance of, or inherits from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance or subclass.
    """
    return isinstance(obj, a_class)
