#!/usr/bin/python3
# 100-safe_print_integer_err.py
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except ValueError as exc:
        print("Exception:", exc, file=sys.stderr)
        return False
