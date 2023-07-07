#!/usr/bin/python3
# 3-say_my_name.py
"""defines a function that prints square"""


def print_square(size):
    """
    Prints a square with the character '#' of the given size length.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
