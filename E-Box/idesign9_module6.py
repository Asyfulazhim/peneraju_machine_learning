'''
Module: First Non-Repeating Character

Sandhya and Pooja are playing string game. And Sandhya gives a string to Pooja, 
and she has to find a first non-repeating character from that string. 
So help Pooja by writing a program to find the first non-repeating character from that string.

Input Format:
The input consists of a string.

Output Format:  
The output consists of a character which represents the first non-repeating character.
If there is no non-repeating character in the string, then print '#'.

Note: All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output 1:
swiiss
w

Sample Input and output 2:
naddan
#
'''

def firstNonRepeatingCharacter(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in s:
        if char_count[char] == 1:
            return char
    return '#'

s = input("Enter the string: ")
print(firstNonRepeatingCharacter(s))