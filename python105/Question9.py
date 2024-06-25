# Problem 9 Roman to Integer
# Write a program to convert a Roman numeral to an integer and also convert integer to Roman numeral
# Roman numerals are represented by seven different symbols: I, V, X, L, C

# def rom2num(arg):
#     roman = input("Enter a Roman numeral: ")
#     roman = roman.upper()
#     roman_dict = {'I': 1, 'V': 5, 'X':
#                   10, 'L': 50, 'C': 100, 'D':
#                   500, 'M': 1000}
#     num = 0
#     for i in range(len(roman) - 1):
#         if roman_dict[roman[i]] < roman_dict[roman[i + 1]]:
#             num -= roman_dict[roman[i]]
#         else:
#             num += roman_dict[roman[i]]
#             num += roman_dict[roman[-1]]
#         print("The integer value of the Roman numeral is: ", num)

# rom2num("IV")

roman = input("Enter Roman Numeral: ")
roman = roman.upper()
roman_dict = {'I': 1, 'V': 5, 'X': 10
              , 'L': 50, 'C': 100, 'D': 500,
              'M': 1000}

def value(v):
    if v == 'I':
        return roman_dict["I"]
    elif v == 'V':
        return roman_dict["V"]
    elif v == 'X':
        return roman_dict["X"]
    elif v == 'L':
        return roman_dict["L"]
    elif v == 'C':
        return roman_dict["C"]
    elif v == 'D':
        return roman_dict["D"]
    elif v == 'M':
        return roman_dict["M"]
    else:
        return 0
    
i = 0
intnum = 0
while i < len (roman):
    p1 = value(roman[i])
    if i + 1 < len(roman):
        p2 = value(roman[i + 1])
        if p1 >= p2:
            intnum += p1
            i += 1
        else:
            intnum += p2 - p1
            i += 2
    else:
        intnum += p1
        i += 1

print(f"{roman} = {intnum}")
    


# print(roman_dict[roman])
# print(roman_dict['X'])