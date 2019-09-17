def max_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        maxnum = my_list[0]
        for i in range(1, len(my_list)):
            if my_list[i] > maxnum:
                maxnum = my_list[i]
        return maxnum
