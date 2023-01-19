#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    result = 0
    length = len(argv)
    if length - 1 == 0:
        print("{}".format(0))
    else:
        for i in range(1, length):
            result += int(argv[i])
        print("{}".format(result))
