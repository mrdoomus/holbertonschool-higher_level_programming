#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    values = sorted(a_dictionary.values())
    maxnum = values[-1]
    for key in a_dictionary:
        if maxnum == a_dictionary[key]:
            return key
