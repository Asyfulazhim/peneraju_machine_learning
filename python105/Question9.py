# Problem 9 Roman to Integer
# Write a program to convert a Roman numeral to an integer and also convert integer to Roman numeral
# Roman numerals are represented by seven different symbols: I, V, X, L, C

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

# convert integer to roman

integer_list = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
rom_list = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

def int_to_rom(roman):
    roman1 = ''
    h = 0
    while h < len(integer_list):
        Quot = roman // integer_list[h]
        roman %= integer_list[h]
        roman1 += rom_list[h] * Quot
        h += 1

    return roman1

intnum1 = int(input("Enter integer: "))
print(int_to_rom(intnum1))