'''
Jack was a little boy, who was playing the game word puzzle. The jack brother gave him a task to find the nouns in a given set of lines. Try to help jack to finish his task.


Problem Constraints:
Use the re  module for Regular Expression
Use the findAll method

Extract all names from the given text. Use metacharacter
Rules:
1) only alphabets
2) starts with upper-case
3) may contain surnames
4) may contain initials

Input format:
A single line input string consists of capitalized words in it.

Output format:
The output will be the words which are obeying the mentioned rules


Sample Input 1:
S.Vinoth Kumar and John Watson are friends with James
Sample output 1:
S.Vinoth Kumar 
John Watson 
James

Sample Input 2:
there were two friends named Sam and Jason
Sample output 2:
Sam
Jason
'''
# import re
# def find_names(text):
#     # Use regular expression to find all names in the text
#     names = re.findall(r'[A-Z][a-z]*(?:\.[A-Z][a-z]*)*(?: [A-Z][a-z]*)*', text)
#     return names

# text = input()
# print(find_names(text))

'''
Ishan playing aa simple game with alphabets. 
the procedure will be Ishan choose aa random number in between (0-26) 
and then he changed the alphabets in Ceaser chipper(Each letter 'shifted'  wrt chosen number).

So can you please help Ishan to write aa program for Ceaser cipher Encryption. Input and Output format Specifications are shown below.

Input Format Specifications:

The first line of Input contains a String.
The next line of input contains Integer N, N is the shifted positions number.
Replace all characters with the nth character from the current character.
 Must use "re.sub()".
Note: [" ord() expected a character, but a string of length 2 found" if the error shows like this then you use the lambda function ].

Output Format Specifications:

Output Consists of String.
if character addition is going greater than 127 then print ‘invalid’.
Sample Input and Output showed below.
Sample Input 1:
amphisoft
3
Sample Output 1:
dpsklvriw

Sample Input 2:
krishnamohan
27
Sample Output 2:
invalid
'''
import re
def ceaser_cipher(text, n):
    
    result = re.sub(r'([a-zA-Z])', lambda m: chr(ord(m.group()) + n) if ord(m.group()) + n <= 127 else 'invalid', text)
    if 'invalid' in result:
        return 'invalid'
    else:
        return result

#text = "amphisoft"
#n = 3
text = input()
n = int(input())
print(ceaser_cipher(text, n))