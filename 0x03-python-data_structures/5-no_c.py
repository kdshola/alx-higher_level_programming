#!/usr/bin/python3
def no_c(my_string):
    string_copy = ""
    for letter in my_string:
        if letter not in "cC":
            string_copy += letter
    return string_copy
