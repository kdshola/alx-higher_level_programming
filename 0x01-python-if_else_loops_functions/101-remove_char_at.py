#!/usr/bin/python3
def remove_char_at(str, n):
    str_cpy = str
    if n >= len(str):
        return str_cpy
    elif n == 0:
        str_cpy = str[1:]
        return str_cpy
    elif n == len(str) - 1:
        str_cpy = str[:-1]
        return str_cpy
    else:
        str_cpy = str[:n] + str[n+1:]
        return str_cpy
