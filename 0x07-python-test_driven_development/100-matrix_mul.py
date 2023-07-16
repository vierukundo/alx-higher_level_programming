#!/usr/bin/python3
# 100-matrix_mul.py
"""function Doc"""


def validate_matrix(matrix, matrix_name):
    """Check if matrix is a list of lists of int/float"""
    if not isinstance(matrix, list):
        raise TypeError(f"{matrix_name} must be a list")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(f"{matrix_name} must be a list of lists")

    if not any(matrix):
        raise ValueError(f"{matrix_name} can't be empty")

    if not all(
            isinstance(element, (int, float))
            for row in matrix for element in row):
        raise TypeError(
                f"{matrix_name} should contain only integers or floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError(f"each row of {matrix_name} must be of the same size")


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices"""

    validate_matrix(m_a, "m_a")
    validate_matrix(m_b, "m_b")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_a[0])))
            row.append(element)
        result.append(row)

    return result
