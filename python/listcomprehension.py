# deepcopy
fruits = ["apple", "orange", "mango","banana", "grapes"]
prices = [1.5, 1.7, 2.2, 3.2, 1.8]
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
pricewithsst = []
for price in prices:
    pricewithsst.append(price * 1.06)
print(pricewithsst)
print("-"*100)

# list comprehension
pricewithsst = [price * 1.06 for price in prices]
print(pricewithsst)
print("="*100)


# Situation 4
# traditional
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
print("="*100)

# situation 5
multipleofthree = []
for number in range(1,50): #list of 50 items
    if number % 3 == 0:
        multipleofthree.append(number)
print(multipleofthree)
print("-"*100)

#list comprehension
multipleofthree = [number for number in range(1,50) if number % 3 == 0]
print(multipleofthree)
print("="*100)

# Situatio 6
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

# list comprehension



