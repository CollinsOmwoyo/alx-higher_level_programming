#!/usr/bin/python3
"""
This module defines the `BaseGeometry` class, basic
geometry-related operations and validation methods.
"""


class BaseGeometry:
    """A class for basic geometry operations and value validation."""

    def area(self):
        """
        Raise an exception to indicate that the area method isn't.

        Raises:
            Exception: Always raised with the message 'area() isn't'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.

        Args:
            name (str): Name of the parameter being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
