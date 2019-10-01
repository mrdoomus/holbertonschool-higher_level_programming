#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as err:
        print("Exception: {}".format(str(err)), file=sys.stderr)
        result = None
    return result
