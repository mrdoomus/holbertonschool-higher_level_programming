#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer(["hola"]))
print(max_integer((1, 3, 6, 2)))
print(max_integer())
print(max_integer([1, 3, 6, 2], 5))
print(max_integer([1.5, 2.5, 3.5, 4.5, 6.5]))
print(max_integer([]))
print(max_integer({1, 3, 7, 2}))
print(max_integer([1, 3, "hi", 2]))
print(max_integer([1, 4, 10, 10]))
