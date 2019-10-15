#!/usr/bin/python3
"""
Class MyInt inverts operators
"""


class MyInt(int):
    def __eq__(self, other):
        return self != other

    def __ne__(self, other):
        return self == other
