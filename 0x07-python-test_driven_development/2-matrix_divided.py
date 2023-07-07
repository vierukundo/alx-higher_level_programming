#!/usr/bin/python3
# 2-matrix_divided.py
"""defines a function that divedes matrix"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number and returns a new matrix.

    Args:
        matrix (list): A matrix represented as a list of lists containing integers or floats.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with elements divided by the given number, rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats or if
        each row of the matrix doesn't have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
