#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        uniq_set = set(my_list)
        uniq_list = list(uniq_set)
        num = uniq_list[0]
        for i in range(1, len(uniq_list)):
            num += uniq_list[i]
        return num
    else:
        return None
