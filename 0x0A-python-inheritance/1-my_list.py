#!/usr/bin/python3
"""
Class Mylist inherits from list
"""


class MyList(list):
    def print_sorted(self):
        """
        Prints a list in ascending order
        """
        print(sorted(self))
