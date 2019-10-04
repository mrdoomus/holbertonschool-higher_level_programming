#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    say_my_name - Prints first and second name
    @first_name: A string
    @last_name: A string
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')
    else:
        print("My name is {} {}".format(first_name, last_name))
