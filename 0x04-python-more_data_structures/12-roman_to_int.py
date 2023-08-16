#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    num_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum_list = [num_dic[i] for i in roman_string]
    total = 0
    for i in range(len(sum_list)):
        total += sum_list[i]
        if sum_list[i - 1] < sum_list[i] and i != 0:
            total -= sum_list[i - 1] + sum_list[i - 1]
    return total
