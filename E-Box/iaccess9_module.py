'''
Input Format:
The first line of input consists of a string.
The next line of input consists of a character.

Output Format:
The output is a list of strings after splitting.
Every first letter of splitted word should be in capital.

Note: All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output 1:
aaahggghbbb
h
Strings after splitting
Aaa
Ggg
Bbb

Sample Input and Output 2:
ahhg&hcg&fhgf90
&
Strings after splitting
Ahhg
Hcg
Fhgf90

'''

wordsstring = input()
splitchar = input()
splittedwords = wordsstring.split(splitchar)
for i in range(len(splittedwords)):
    splittedwords[i] = splittedwords[i].capitalize()
for word in splittedwords:
    print(word)
print(splittedwords)

'''
Module: Continuous Prime Sum
In Maple Casino, there is a play in which contestant hit a ball to two numbered plates, and then contestant has to say a number which is summation of all the prime numbers from 1 to 'n' , here 'n' represent the first plate number. And the operation will continue upto 't' times, here 't' represent the second plate number.

Explanation:
First we perform the sum operation of all the prime numbers from 1 to 7 i.e. {2,3,5,7}, the sum of these prime numbers is: 17.
Then, again we have to perform the sum of all the prime numbers from 1 to 17, which is the previous sum of prime numbers.
1 to 17: {2,3,5,7,11,13,17}, and the resultant sum of prime numbers is: 58.
This operation will continue upto 2 times (for above mentioned sample input).

Write a program to find the continous sum of prime numbers 't' times.

Input Format:
First line as integer which corresponds to last integer of prime series.
Second line as integer which corresponds to number of times we have to perform the sum operation of that prime series.

Output Format:
A line as integer which corresponds to sum of all the prime numbers.

Input Format:
7
2
Output Format:
Sum:58

'''
#prime numbers
def isprime(n):
    if n==1:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True

num1= int(input())
num2= int(input())
count = 0

while count < num2:
    sum = 0
    for i in range(1,num1+1):
        if isprime(i):
            sum+=i
    num1 = sum
    count+=1
      
print(f"Sum:{sum}")





