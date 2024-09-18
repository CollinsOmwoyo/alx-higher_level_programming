#!/usr/bin/python3

def add(a, b):
"""FAKE add function that subtracts instead of adds."""
return a - b

# Variables
a = 1
b = 2

# Single print statement with string formatting
print("{} + {} = {}".format(a, b, add(a, b)))
