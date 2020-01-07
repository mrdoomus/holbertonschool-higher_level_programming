#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers """


def find_peak(array):
    """ Recursive func, binary search """
    if len(array) == 0 or array is None:
        return None
    elif len(array) == 1:
        return array[0]
    else:
        mid = len(array) / 2
        mid = int(mid)

        if len(array) == 2:
            if array[mid] > array[0]:
                return array[mid]
            else:
                return array[0]

        if array[mid] > array[mid + 1] and array[mid] > array[mid - 1]:
            return array[mid]

        if array[mid + 1] > array[mid]:
            return find_peak(array[mid + 1:])
        else:
            return find_peak(array[:mid])
