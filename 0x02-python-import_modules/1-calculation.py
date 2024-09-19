#!/usr/bin/python3
# Importing functions here
from calculator_1 import add, sub, mul, div

# Variables
a = 10
b = 5

# Performing operations
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
