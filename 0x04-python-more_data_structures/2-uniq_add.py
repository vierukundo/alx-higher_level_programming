#!/usr/bin/python3
# 2-uniq_add.py
def uniq_add(my_list=[]):
    """function that adds all unique integers in a list"""
    sum_of_unique_int = 0
    for num in set(my_list):
        sum_of_unique_int += num
    return sum_of_unique_int
