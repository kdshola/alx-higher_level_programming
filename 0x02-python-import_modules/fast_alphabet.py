#!/usr/bin/python3
def alphabets():
    for i in range(26):
        print("{:s}".format(chr(i + 65)), end="")
    print()
