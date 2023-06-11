#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Function that prints matrix rows per line"""
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print()
    for row in matrix:
        for i in range(len(row)):
            if i < len(row) - 1:
                print("{:d}".format(row[i]), end=" ")
            else:
                print("{:d}".format(row[i]))
