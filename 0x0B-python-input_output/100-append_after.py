#!/usr/bin/python3
# 100-append_after.py
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
