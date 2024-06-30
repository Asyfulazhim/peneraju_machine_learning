# Raj wants to generate some random numbers for creating a new PIN for his debit card, every month. 
# So he developed Program such a way that, he will enter list random numbers which are having duplicate elements 
# and it will return a set of distinct elements from that, 
# he will generate a new PIN for his card.

# Input and Output Format:
# 1st input is a number indicates a total number of elements in the list.
# 2nd input is a String contains a list of numbers.
# 3rd input is number indicates K (number of elements need to sum every time)
# The output contains a set of elements after summing. ( Refer to sample output format).

# Sample Input and Output 1:
# 9
# 1 3 2 4 5 1 6 31 15
# [1, 2, 3, 4, 5, 6, 15, 31]
# 3
# [6, 15, 31]



def calculate_size(num):
    if num % 3 == 0:
        size = int(num / 3)
    else:
        size = int(num / 3) + 1
    return size

def convToSet(numlist):
    newlist = list(map(int, numlist))
    newlist = list(set(newlist))
    #print("newlist",newlist)
    return newlist

def SumItem(list, size):
    sumlist = []
    while len(list) >= size:
        sum = 0
        for i in range(size):
            sum += list[0]
            list.pop(0)
        sumlist.append(sum)
    else:
        for i in list:
            sumlist.append(i)
    finallist = list(set(sumlist))
    #print(finallist)
    return finallist

def main(rand):
    print(rand)
    size = calculate_size(rand)
    num = input().split()
    list = convToSet(num)
    #print("list",list)
    SumItem(list, size)

import random
rand = random.randint(1,10)
main(rand)
