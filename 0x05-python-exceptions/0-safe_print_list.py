#!/usr/bin/python3
# 0-safe_print_list.py
def safe_print_list(my_list=[], x=0):
    """prints x elements of a list"""
    count = 0
    for index in range(x):
        try:
            if index == x - 1:
                print('{}'.format(my_list[index]))
            else:
                print('{}'.format(my_list[index]), end="")
            count += 1
        except IndexError:
            print()
            break
    return count
