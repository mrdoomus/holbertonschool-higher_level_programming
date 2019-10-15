#!/usr/bin/python3
from builtins import __import__

Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())
