'''
Write a program to get size of list and its elements and  to find numbers divisible by thirteen from a list using anonymous function (Lambda) and display those numbers.

Input Format:
The first line of input corresponds to the size of list 'n'.
The next 'n' line of input corresponds to the elements in the list .

Output Format:
The output consists of numbers divisible by thirteen separated by space.
Refer sample output for formatting specifications.

Problem Constraints:
n > 0 print the numbers divisible by thirteen separated by space, else display as "Invalid input".

Sample Input/Output 1:
Enter size of list
9
Enter the elements in list
12
65
54
39
102
339
221
50
70
65 39 221

Sample Input/Output 2:
Enter size of list
O
Invalid input
'''
n = int(input("Enter size of list\n"))
if(n <= 0):print("Invalid input")
else:
    list = []
    print("Enter the elements in list")
    for i in range(n):
        list.append(int(input()))
    print(*filter(lambda x: x % 13 == 0, list))


