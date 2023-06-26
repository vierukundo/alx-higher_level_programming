#!/usr/bin/python3
# 0-safe_print_list.py
def safe_print_list(my_list=[], x=0):
    """prints x elements of a list"""
    try:
        for index in range(x):
            if index == x - 1:
                print('{}'.format(my_list[index]))
                return x
            else:
                print('{}'.format(my_list[index]), end="")
    except IndexError:
        print()
        return index
