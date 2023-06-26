#!/usr/bin/python3
# 2-safe_print_list_integers.py
def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers"""
    count = 0
    try:
        for i in range(x):
            if type(my_list[i]) != int:
                continue
            else:
                if i == x - 1:
                    print("{:d}".format(my_list[i]))
                else:
                    print("{:d}".format(my_list[i]), end="")
                count += 1
    except(IndexError, Exception):
        print()
    return count
