#!/usr/bin/python3
# 5-raise_exception.py
def raise_exception():
    """raises a type exception"""
    try:
        raise TypeError("raising error")
    except TypeError:
        raise
