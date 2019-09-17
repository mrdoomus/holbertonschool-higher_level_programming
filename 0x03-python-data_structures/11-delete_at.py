#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= len(my_list) or idx < 0:
        return my_list
    else:
        num = my_list[idx]
        my_list.remove(num)
    return my_list
