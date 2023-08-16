#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_copy = my_list[:]
    for i in range(len(my_list)):
        if list_copy[i] == search:
            list_copy[i] = replace
    return list_copy
