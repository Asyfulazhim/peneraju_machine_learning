# Problem 9 Roman to Integer
# Write a program to convert a Roman numeral to an integer and also convert integer to Roman numeral
# Roman numerals are represented by seven different symbols: I, V, X, L, C

def rom2num(arg):
    roman = input("Enter a Roman numeral: ")
    roman = roman.upper()
    roman_dict = {'I': 1, 'V': 5, 'X':
                  10, 'L': 50, 'C': 100, 'D':
                  500, 'M': 1000}
    num = 0
    for i in range(len(roman) - 1):
        if roman_dict[roman[i]] < roman_dict[roman[i + 1]]:
            num -= roman_dict[roman[i]]
        else:
            num += roman_dict[roman[i]]
            num += roman_dict[roman[-1]]
        print("The integer value of the Roman numeral is: ", num)

rom2num("IV")
    