#!/usr/bin/python3
# 101-safe_function.py
def safe_function(fct, *args):
    """function that executes a function safely"""
    import sys
    try:
        result = fct(args[0], args[1])
        return result
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
