#!/usr/bin/python3
# 1-search_replace.py
def search_replace(my_list, search, replace):
    """Search and replace"""
    new_list = list(map((lambda x: replace if x == search else x), my_list))
    return new_list
