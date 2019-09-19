#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        return max(a_dictionary)
    #values = sorted(a_dictionary.values())
    #print(values)
    #res = values[-1]
    #print(res)
    #for key in a_dictionary:
        #if res == a_dictionary[key]:
            #return key
