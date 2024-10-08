#!/usr/bin/python3
"""
Alright, let's divide a matrix! It's math time.
"""

def matrix_divided(matrix, div):
    """
    Splits everything in your matrix into smaller bits.
    Args:
        matrix (list of lists): Your matrix of numbers (integers or floats).
        div (int or float): The number we’re using to split everything.
    Returns:
        list: A new matrix with all values divided and rounded to 2 decimal places.
    """
    if not all(isinstance(row, list) for row in matrix) or \
       not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in row] for row in matrix]
