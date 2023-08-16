#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = set(my_list)
    total = 0
    for num in add:
        total += num
    return total
