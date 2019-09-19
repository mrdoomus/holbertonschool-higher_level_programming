#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        for key in a_dictionary:
            if a_dictionary[key] is 0:
                return None
        return max(a_dictionary)
