#!/usr/bin/python3
class MyList(list):
    """Inherits list and implements a sorted print function."""
    
    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
