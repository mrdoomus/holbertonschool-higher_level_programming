#!/usr/bin/python3
"""
Class MyInt inverts operators
"""


class MyInt(int):
    def __eq__(self, other):
        """
        Changes == to !=
        """
        return int(self) != int(other)

    def __ne__(self, other):
        """
        Changes != to ==
        """
        return int(self) == int(other)
