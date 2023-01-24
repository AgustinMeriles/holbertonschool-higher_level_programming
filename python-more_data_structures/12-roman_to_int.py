#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    else:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        for i in range(len(roman_string)):
            a = roman_string[i]
            b = roman_string[i - 1]
            if i > 0 and translations[a] > translations[b]:
                number += translations[a] - 2 * translations[b]
            else:
                number += translations[a]
        return number
