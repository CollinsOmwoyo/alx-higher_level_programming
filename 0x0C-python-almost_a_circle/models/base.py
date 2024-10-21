#!/usr/bin/python3
"""
This module defines the Base class, which serves as the foundation
for other geometric shapes (Rectangle, Square). It provides functionality
for managing instance IDs and handling JSON serialization and deserialization.

Classes:
    - Base: A base class for managing IDs and JSON operations.
"""

import json


class Base:
    """Represents the base class for other shapes, managing IDs.

    Attributes:
        __nb_objects (int): A counter for the number of objects created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int, optional): The identity of the instance. If None,
                an auto-generated ID will be assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of the list.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string back into a list of dictionaries.

        Args:
            json_string (str): A JSON string representation.

        Returns:
            list: A list of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of instances to a JSON file.

        Args:
            list_objs (list): A list of instances (Rectangle/Square).
        """
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]
            ))

    @classmethod
    def load_from_file(cls):
        """Loads instances from a JSON file.

        Returns:
            list: A list of instances.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as f:
                list_dicts = cls.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Creates a new instance with attributes from a dictionary.

        Args:
            **dictionary: Keyworded arguments representing attributes.

        Returns:
            object: A new instance with the specified attributes.
        """
        dummy = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dummy.update(**dictionary)
        return dummy
