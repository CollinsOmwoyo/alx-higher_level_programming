#!/usr/bin/python3
"""
This module defines the Square class, which inherits from Rectangle.
The class represents a square—a specialized form of a rectangle with
equal width and height. It includes methods to manipulate, display,
and update square attributes.

Classes:
    - Square: A class representing a square.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, inheriting from Rectangle.

    Attributes:
        size (int): The size of the square's sides (width and height).
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The identity of the square instance.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square's sides.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int, optional): The identity of the square instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute.

        Args:
            value (int): The new size of the square's sides.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates attributes of the square instance.

        Args:
            *args: No-keyword arguments to update attributes in
                the following order:
                1st - id, 2nd - size, 3rd - x, 4th - y.
            **kwargs: Keyword arguments representing attributes
                to be updated. If *args is provided, **kwargs
                will be ignored.
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the square.

        Returns:
            dict: A dictionary containing the attributes of the square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Returns a string representation of the square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
