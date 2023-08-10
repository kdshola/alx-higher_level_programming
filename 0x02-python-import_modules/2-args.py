#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv_length = len(argv) - 1
    if argv_length == 0:
        print("0 arguments")
    elif argv_length == 1:
        print("1 argument")
        print("{:d}: {:s}".format(argv_length, argv[1]))
    else:
        print("{} arguments".format(argv_length))
        for num in range(argv_length):
            print("{:d}: {:s}".format(num + 1, argv[num + 1]))
