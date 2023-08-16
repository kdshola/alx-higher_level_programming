#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    add = 0
    div = 0
    for tup in my_list:
        add += tup[0] * tup[1]
        div += tup[1]
    return add / div
