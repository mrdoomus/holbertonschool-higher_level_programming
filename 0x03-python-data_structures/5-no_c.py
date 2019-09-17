#!/usr/bin/python3
def no_c(my_string):
    str_list = list(my_string)
    tmp = ""
    for i in str_list:
        if i == 'c':
            str_list.remove('c')
        elif i == 'C':
            C = str_list.remove('C')
    my_string = tmp.join(str_list)
    return my_string
