#!/usr/bin/python3
"""
This module defines the `inherits_from` function, which checks if an object
is an instance of a subclass of a specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a subclass of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of a subclass of the class,
            but not an instance of the class itself. Otherwise, False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
