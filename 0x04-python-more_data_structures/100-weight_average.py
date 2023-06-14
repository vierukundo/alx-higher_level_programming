#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    mul = 0
    d = 0

    for tup in my_list:
        mul += tup[0] * tup[1]
        d += tup[1]

    return (mul / d)
