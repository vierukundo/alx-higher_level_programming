#!/usr/bin/python3
# 9-multiply_by_2.py
def multiply_by_2(a_dictionary):
    """returns a new dictionary with all values multiplied by 2"""
    list_of_values = []
    for key, value in a_dictionary.items():
        list_of_values.append((key, value * 2))
    return dict(list_of_values)
