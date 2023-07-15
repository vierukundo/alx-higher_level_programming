#!/usr/bin/python3
# 3-say_my_name.py
"""function definition"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If first_name is not a string or last_name is not a string.
    """
    if first_name is None or not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = first_name + " " + last_name

    print("My name is", full_name)
