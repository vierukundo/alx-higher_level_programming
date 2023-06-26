#!/usr/bin/python3
# 6-raise_exception_msg.py
def raise_exception_msg(message=""):
    """raises a name exception with a message"""

    try:
        raise NameError(message)
    except NameError:
        raise
