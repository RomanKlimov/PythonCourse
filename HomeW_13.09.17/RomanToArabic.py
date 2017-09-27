RomanDict = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}


def roman_to_arabic(roman):
    part_sum = 0
    full_sum = 0
    previous_digit = 0

    for char in roman:
        if RomanDict[char] == previous_digit:
            part_sum += RomanDict[char]

        elif RomanDict[char] > previous_digit:
            full_sum -= part_sum
            part_sum = RomanDict[char]
            previous_digit = RomanDict[char]

        elif RomanDict[char] < previous_digit:
            part_sum += RomanDict[char]
            previous_digit = RomanDict[char]
    full_sum +=part_sum
    print(full_sum)

roman_to_arabic('DCC')


