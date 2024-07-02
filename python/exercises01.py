#Given the number 97531
#reverse the number
#expected result 13579
''''
a0 = 97531
result = a0 % 10
a1 = a0 // 10
print(result, a1)

result = (result * 10) + (a1 % 10)
a2 = a1 // 10
print(result, a2)

result = (result * 10) + (a2 % 10)
a3 = a2 // 10
print(result, a3)

result = (result * 10) + (a3 % 10)
a4 = a3 // 10
print(result, a4)

result = (result * 10) + (a4 % 10)
a5 = a4 // 10
print(result, a5)
'''

#Akmal solution
'''
result1 = (a0 % 10)* 10000
result1 = result1 + ((a0 // 10) % 10)*1000 
print(result1)
'''

givenNumber = 97531
result = 0
result = (result * 10) + givenNumber % 10
#result *= 10 + (givenNumber % 10)
givenNumber //= 10
result *= 10 + (givenNumber % 10)
print(result)


#How to reset not using if condition
#by using remainder or modulud
'''
currentDay = 0
totalDay = 5
print(currentDay % totalDay)
currentDay = currentDay + 1
print(currentDay % totalDay)
currentDay = currentDay + 1
print(currentDay % totalDay)
currentDay = currentDay + 1
print(currentDay % totalDay)
currentDay = currentDay + 1
print(currentDay % totalDay)
currentDay = currentDay + 1
print(currentDay % totalDay)
currentDay = currentDay + 1
print(currentDay % totalDay)
currentDay = currentDay + 1
print(currentDay % totalDay)
currentDay = currentDay + 1
'''

nestedlist = [
    [1, 2, 3],
    [3, 4, 5],
    [1, 2, 3]
]

nestedlist = [tuple(item) for item in nestedlist]
print(set(nestedlist))