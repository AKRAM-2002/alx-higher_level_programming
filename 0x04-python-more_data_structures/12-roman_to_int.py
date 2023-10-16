#!/usr/bin/python3
def roman_to_int(roman_string):
    #roman number -> largest to smallest: add them up (+)
    # IF smallest before larger: substract smaller (-)

    roman_numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D":500,
        "M":1000
    }

    if not isinstance(roman_string,str):
        return 0

    sum = 0


    for i in range(len(roman_string)):
        if i + 1 < len(roman_string) and roman_numbers[roman_string[i]] < roman_numbers[roman_string[i+1]]:
            sum -= roman_numbers[roman_string[i]]
        else:
            sum += roman_numbers[roman_string[i]]



    return sum
