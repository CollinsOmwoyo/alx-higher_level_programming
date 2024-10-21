#!/usr/bin/python3
"""
This module defines the Rectangle class, which inherits from Base.
The class represents a geometric rectangle with features like
width, height, x, y positions, and an id. It provides functionalities
to calculate area, display the rectangle, update attributes, and
represent the instance as a dictionary.

Classes:
    - Rectangle: A class representing a rectangle.
"""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle that inherits from Base class.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
        id (int): The identity of the rectangle instance.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int, optional): The identity of the rectangle instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def update(self, *args, **kwargs):
        """Updates attributes of the rectangle instance.

        Args:
            *args: No-keyword arguments that update attributes
                in the following order:
                1st - id, 2nd - width, 3rd - height,
                4th - x, 5th - y.
            **kwargs: Keyword arguments representing attributes
                to be updated. If *args is provided, **kwargs
                will be ignored.
        """
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the rectangle.

        Returns:
            dict: A dictionary containing the attributes of the rectangle.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Returns a string representation of the rectangle instance."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
