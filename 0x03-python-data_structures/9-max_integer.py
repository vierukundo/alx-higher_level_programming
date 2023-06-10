#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    for num1 in my_list:
        flag = 0
        for num2 in my_list:
            if num1 < num2:
                flag = 1
        if flag == 0:
            return num1
