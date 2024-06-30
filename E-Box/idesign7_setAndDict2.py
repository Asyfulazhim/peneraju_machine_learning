# Input and Output Format:
# Input is a string.
# The output contains dictionary representation in ascending order of characters 
# and occurrence of each character in a string (Refer sample output format).

# All text in bold corresponds to the input and the rest corresponds to output
# [Refer sample input and output format].

# Sample Input 1:
# sandhyaa
# Sample Output 1:
# Dictionary of string: {'a': 3, 'd': 1, 'h': 1, 'n': 1, 's': 1, 'y': 1}
# a-- 3
# d-- 1
# h-- 1
# n-- 1
# s-- 1
# y-- 1

# Sample Input 2:
# aaaattttgggjjjiiibb
# Sample Output 2:
# Dictionary of string: {'a': 4, 'b': 2, 'g': 3, 'i': 3, 'j': 3, 't': 4}
# a-- 4
# b-- 2
# g-- 3
# i-- 3
# j-- 3
# t-- 4

# Sample Input 3:
# rathhaann
# Sample Output 3:

# Dictionary of string: {'a': 3, 'h': 2, 'r': 1, 't': 1, 'n': 2}
# a-- 3
# h-- 2
# n-- 2
# r-- 1
# t-- 1

def check_in_dict(n):
    dict = {}
    for i in sorted(n):
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(f"Dictionary of string: {dict}")
    return dict

def print_char(c):
    for i in sorted(c):
        print(f"{i}--{c[i]}")

n = input()
dict = check_in_dict(n)
print_char(dict)