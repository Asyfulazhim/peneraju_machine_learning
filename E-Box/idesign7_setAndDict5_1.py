def take_input(n):
    inputs_str = " ".join([input() for _ in range(n)])
    inputs = list(map(int, inputs_str.split()))
    return inputs

def calculate_size(num):
    if num % 3 == 0:
        size = int(num / 3)
    else:
        size = int(num / 3) + 1
    print(size)
    return size

def convToSet(numlist):
    newlist = list(map(int, numlist))
    newlist = list(set(numlist))
    newlist.sort()
    print(newlist)
    return newlist

def SumItem(numlist, size):
    sumlist = []
    while len(numlist) >= size:
        sum = 0
        for i in range(size):
            sum += numlist[0]
            numlist.pop(0)
        sumlist.append(sum)
    else:
        for i in numlist:
            sumlist.append(i)
    #print("Sumlist", sumlist)
    finallist = list(set(sumlist))
    finallist.sort()
    print(finallist)
    return finallist

def main(rand):
    print(rand)
    inputs = take_input(rand)
    #num = input().split()
    numlist = convToSet(inputs)
    size = calculate_size(len(numlist))
    #print("list",list)
    SumItem(numlist, size)

import random
rand = random.randint(5,10)
main(rand)