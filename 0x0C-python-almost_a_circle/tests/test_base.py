"""
Unit tests for the Base class in the models package.

The Base class provides the foundation for other geometric shapes, 
offering functionalities such as automatic ID assignment and JSON 
serialization.
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_auto_id_assignment(self):
        """Test that IDs are assigned automatically in sequence."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_custom_id_assignment(self):
        """Test that custom IDs are assigned correctly."""
        b = Base(42)
        self.assertEqual(b.id, 42)

    def test_to_json_string(self):
        """Test the JSON string representation of a list of dictionaries."""
        dict_list = [{'id': 1}, {'id': 2}]
        json_str = Base.to_json_string(dict_list)
        self.assertEqual(json_str, '[{"id": 1}, {"id": 2}]')

    def test_from_json_string(self):
        """Test conversion from JSON string to a list of dictionaries."""
        json_str = '[{"id": 1}, {"id": 2}]'
        dict_list = Base.from_json_string(json_str)
        self.assertEqual(dict_list, [{'id': 1}, {'id': 2}])

if __name__ == '__main__':
    unittest.main()
