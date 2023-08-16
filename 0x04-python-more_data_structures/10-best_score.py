#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return
    key_list = list(a_dictionary.keys())
    value_list = list(a_dictionary.values())
    return key_list[value_list.index(max(value_list))]
