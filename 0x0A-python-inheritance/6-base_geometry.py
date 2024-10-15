#!/usr/bin/python3
"""
This module defines the `BaseGeometry` class, a template
for geometry-related operations.
"""


class BaseGeometry:
    """A class for basic geometry operations."""

    def area(self):
        """
        Raise an exception to indicate that the area method isn't.

        Raises:
            Exception: Always raised with the message 'area() isn't'.
        """
        raise Exception("area() is not implemented")
