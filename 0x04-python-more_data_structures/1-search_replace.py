#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        new_list = list(map(lambda n: replace if n == search else n, my_list))
        return new_list
    else:
        return None
