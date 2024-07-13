'''
Finding covariance

Create two lists consists of integers,each of size 5 and then find the covariance and print.
Input format:
First 5 lines of input corresponds to elements of list 1.
Next 5 lines of input corresponds to elements of list 2.

Output format:
Output corresponds to covariance between lists.

Sample Input:
6 5 3 9 1 0 5 9 78 2

Sample Output:
76.2
'''
import numpy as np

num = input().split(" ")
num = list(map(int, num))

list1 = []
list2 = []
for i in range(len(num)):
    if i < 5:
        list1.append(num[i])
    else:
        list2.append(num[i])

#print(list1)
#print(list2)

covariance = np.cov(list1, list2)[0, 1]
# Print result
print(round(covariance, 1))

