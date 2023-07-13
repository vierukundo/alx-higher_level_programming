#!/usr/bin/python3
# 1-my_list.py
"""class that inherits from list"""


class MyList(list):
    """representation of a list subclass"""
    def __init__(self, *args):
        """Initialization of list subclasss"""
        super().__init__(args)

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
