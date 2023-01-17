#!/usr/bin/python3
def uppercase(str):
    letM = ""
    stringM = ""
    large = len(str)

    for i in range(large):
        letM = ord(str[i])
        if letM >= 97 and letM <= 122:
            letM = letM - 32
        stringM += chr(letM)
    print("{}".format(stringM))
