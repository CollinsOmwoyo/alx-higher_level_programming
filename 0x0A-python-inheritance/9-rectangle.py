#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represents a rectangle with area and string description."""

    def __init__(self, width, height):
        """Initializes the width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the rectangle description."""
        return f"[Rectangle] {self.__width}/{self.__height}"
