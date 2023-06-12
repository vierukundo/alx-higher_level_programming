#!/usr/bin/python3
def no_c(my_string):
    str_list = [char for char in my_string]
    for element in str_list:
        if element == 'c' or element == 'C':
            str_list.remove(element)
    new_str = ''.join(str_list)
    return str(new_str)
