#!/usr/bin/python3
# 0-read_file.py
"""function definition"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="UTF8") as f:
        print(f.read(), end="")
