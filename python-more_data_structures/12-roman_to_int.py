#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for char in roman_string:
        value = roman_map[char]

        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value

        prev_value = value

    return total
