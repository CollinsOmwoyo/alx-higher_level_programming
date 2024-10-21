"""
This module initializes the models package, which contains the definitions
of geometric shapes and the base class. The package provides functionality
for creating, manipulating, and managing rectangles, squares, and the base
objects, along with JSON serialization.

Modules:
    - base: Defines the Base class, which serves as the foundation for other shapes.
    - rectangle: Defines the Rectangle class, a geometric shape with width and height.
    - square: Defines the Square class, a specialized rectangle with equal sides.
"""

# Import classes to ensure they are accessible when importing the package.
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

__all__ = ['Base', 'Rectangle', 'Square']
