#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print()
    for row in matrix:
        for i in range(len(row)):
            if i < len(row) - 1:
                print("{}".format(row[i]), end=" ")
            else:
                print("{}".format(row[i]))
