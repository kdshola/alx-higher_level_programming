#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    key_list = new_dic.keys()
    for key in key_list:
        new_dic[key] *= 2
    return new_dic
