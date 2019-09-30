#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length
    res, cnt = 0, 0
    for i in range(list_length):
        try:
            res = my_list_1[cnt] / my_list_2[cnt]
        except ZeroDivisionError:
            res = 0.0
            print("division by 0")
        except TypeError:
            res = 0.0
            print("wrong type")
        except IndexError:
            res = 0.0
            print("out of range")
        finally:
            new_list[cnt] = res
            cnt += 1
    return new_list
