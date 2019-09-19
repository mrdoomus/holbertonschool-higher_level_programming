#!/usr/bin/python3
def roman_to_int(roman_string):
    if not type(roman_string) is str or roman_string is None:
        return 0
    rev = roman_string[::-1]
    value = 0
    if rev[0] != 'I':
        roman_dic_minus = {'I': -1, 'V': 5, 'X': 10, 'L': 50,
                           'C': 100, 'D': 500, 'M': 1000}
        for i in roman_string:
            value += roman_dic_minus[i]
    else:
        roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
        for i in roman_string:
            value += roman_dic[i]
    return value
