# deepcopy
fruits = ["apple", "orange", "mango","banana", "grapes"]

# overseafruits = fruits.copy()

# situation 1
# for loop with list
overseafruits = []
for fruit in fruits:
    overseafruits.append(fruit)
print("-"*100)

# Situation 2
# for loop with some statement
overseafruits = []
for fruit in fruits:
    if fruit != "banana":
        overseafruits.append(fruit)
print(overseafruits)
print("-"*100)

#list comprehension
overseafruits = [fruit for fruit in fruits if fruit != "banana"]
print(overseafruits)
print("="*100)

#tuple comprehension
overseafruits = tuple(fruit for fruit in fruits if fruit != "banana")
print(overseafruits)


# Situation 3
prices = [1.5, 1.7, 2.2, 3.2, 1.8]
pricewithsst = []
for price in prices:
    pricewithsst.append(price * 1.06)
print(pricewithsst)
print("-"*100)

# list comprehension
pricewithsst = [price * 1.06 for price in prices]
print(pricewithsst)
print("="*100)

# create a function
def calculateSST(prices):
    pricewithsst = price + price *0.06
    return pricewithsst

# map function
pricewithsst = list(map(calculateSST, prices))
print(pricewithsst)
# what map does?
# there is for loop in map

# def map(func, values):
#     result = []
#     for value in values:
#         result.append(func(value))
#     return result

# Situation 4
# traditional
print("Celcius to Fahrenheit")
celciusvalues = []
fahrenheitvalues = [32, 212, 100, 212, 90, 0]
for fahrenheit in fahrenheitvalues:
    celciusvalues.append((fahrenheit - 32) * 5/9)
print(celciusvalues)
print("-"*100)

#list comprehension
#instead of writing the traditinally for loops
# we can use list comprehension
# syntax: [expression for item in iterable]
celciusvalues = [(fahrenheit - 32) * 5/9 for fahrenheit in  fahrenheitvalues]
print(celciusvalues)
print("-"*100)

# map function
def fahrenheitToCelcius(fahrenheit):
    return (fahrenheit - 32) * 5/9
celciusvalues = list(map(fahrenheitToCelcius, fahrenheitvalues))
print(celciusvalues)
print("="*100)

# situation 5
print("Multiple Three")
multipleofthree = []
for number in range(1,50): #list of 50 items
    if number % 3 == 0:
        multipleofthree.append(number)
print(multipleofthree)
print("-"*100)

#list comprehension
multipleofthree = [number for number in range(1,50) if number % 3 == 0]
print(multipleofthree)
print("-"*100)

# filter function
# always return boolean value
def findMultipleOfThree(number):
    return True if (number % 3 == 0) else False

multipleofthree = list(filter(findMultipleOfThree, range(1,50)))
print(multipleofthree)
print("="*100)

# Situatio 6
print("Odd Number")
numbers = [2,5,7,3,4,6,10,11,15,17,24,22]
oddnumbers = []
for number in numbers:
    if number % 2 != 0:
        oddnumbers.append(number)
print(oddnumbers)
print("-"*100)

#list comprehension
oddnumbers = [number for number in numbers if number % 2 != 0]
print(oddnumbers)
print("-"*100)

# filter class used when
# we want to filter out certain items from a list
# if the list of input and list of output is difference
# filter class is used
def findOddNumbers(number):
    return True if (number % 2 != 0) else False
oddnumbers = list(filter(findOddNumbers, numbers))
print(oddnumbers)
print("="*100)

# Situation 7
sum = 0
for number in range(1,11):
    sum += number
print("Sum:", sum)
print("-"*100)

# calculate mean value 1 -10 using for loop
meanvalue = 0
for number in range(1,11):
    meanvalue += number
meanvalue /= len(range(1,11))
print(f"{meanvalue:.2f}")
print("="*100)

# Reduce
# built in function
from functools import reduce
print("Reduce Function:")
numbers = [1,2,3]
def findTotal(oldValue, currentValue):
    return oldValue + currentValue
print(reduce(findTotal, numbers))
print("="*100)

# find factorial
print("Find Factorial")
def factorial(oldValue, currentVAlue):
    return oldValue * currentVAlue
print(reduce(factorial, numbers))