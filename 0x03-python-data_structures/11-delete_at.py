#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list == []:
        return None
    else:
        num = my_list[idx]
        my_list.remove(num)
    return my_list
