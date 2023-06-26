#!/usr/bin/python3
# 1-safe_print_integer.py
def safe_print_integer(value):
    """function that prints an integer"""
    try:
        print("{:d}".format(value))
        return True
    except(TypeError, Exception):
        return False
