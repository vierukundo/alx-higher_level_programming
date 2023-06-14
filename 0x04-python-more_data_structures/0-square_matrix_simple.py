#!/usr/bin/python3
# 0-square_matrix_simple.py
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix"""
    new_matrix = []
    for row in matrix:
        new_row = list(map(lambda x: x ** 2, row))
        new_matrix.append(new_row)
    return new_matrix
