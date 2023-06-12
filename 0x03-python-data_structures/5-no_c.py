#!/usr/bin/python3
#5-no_c.py
def no_c(my_string):
    "prints string without character c and C"
    str_list = [char for char in my_string if char != 'c' and char != 'C']
    new_str = ''.join(str_list)
    return new_str
