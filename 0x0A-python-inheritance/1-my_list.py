#!/usr/bin/python3
"""Module containing MyList class that extends list."""

class MyList(list):
    """Class inherits list and implements a sorted print."""
    
    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
