#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_list = []
    tuple_a_list = list(tuple_a)
    tuple_b_list = list(tuple_b)
    if len(tuple_a) < 2:
        tuple_a_list.append(0)
        tuple_a_list.append(0)
    elif len(tuple_b) < 2:
        tuple_b_list.append(0)
        tuple_b_list.append(0)
    for i in range(2):
        tuple_list.append(tuple_a_list[i] + tuple_b_list[i])
    tuple_added = tuple(tuple_list)
    return tuple_added
