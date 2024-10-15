#!/usr/bin/python3
"""
This module defines the `lookup` function, which retrieves all
attributes and methods available for a given object.
"""


def lookup(obj):
    """
    Retrieve a list of all attributes and methods of the provided object.

    Args:
        obj: The object to inspect.

    Returns:
        List of attribute and method names available in the object.
    """
    return dir(obj)
