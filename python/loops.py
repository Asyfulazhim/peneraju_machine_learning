# Whenever you want to iterate a list of items then you must use for loop
fruits = ["apple", "rambutan", "orange", "durian", "mango", "cempedak", "banana", "mangosteen", "grapes"]
# print all the items in the list
for fruit in fruits:
    print(fruit)

# print all the items in the even position
for fruit in fruits[::2]:
    print(fruit)

# print only fruits with 6 letters
for fruit in fruits:
    if (len(fruit) == 6):
        print(fruit)

# I want to print each fruit together with the idex (position)
position = 0
for fruit in fruits:
    print(position, fruit)
    position += 1

# I want to create a multiplication table of 5
# I want to go until 12
# 1 x 5 = 5
# 2 x 5 = 10
multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
multiplicant = 5
for multiplier in multipliers:
    print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)

# however this is not practical when the until is 200 instead of 12
# we have to go for range option start_index:end_index
# but the : operator can work only on an list fruits[2:5]
# we have a built in function called range which can generate list of numbers
# range function takes start index and end index and generate numbers between them
# start index is included end index is not included
print(range(1, 12))
# however when i print it I am not able to see the numbers

# range is an iterable object, 
# which means we can use it in a for loop together with "in" operator
# however print function do not know how to iterate range object
# so it prints as range(1, 12)
# any iterable object can be typecast to a list using list function
# print function knows how to iterate the list
print(list(range(1, 12)))

# let us do the multiplication table using range
multiplicant = 6
for multiplier in range(1, 13):
    print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)

# Split the digits in the input number and print them
# lets say the user give input 97409
# take the input and print 9, 7, 4, 0, 9
# since we do not have it as a list and we also do not know the number of digits
# we have to use while loop
# givenNumber = input("Give me the number: ")
givenNumber = 12345
while (givenNumber > 0):
    print(givenNumber % 10)
    # givenNumber //= 10
    givenNumber = givenNumber // 10

givenNumber = 12345
numberofdigit = len(str(givenNumber)) - 1
while (givenNumber > 0):
    print(givenNumber // 10 ** numberofdigit)
    givenNumber %= 10 ** numberofdigit
    numberofdigit -= 1

givenNumber = 67891
strGivenNumber = str(givenNumber)
for digit in strGivenNumber:
    print(digit)

# for loop and while loop can have else block
fruits = ["apple", "orange", "mango", "banana", "grapes"]
# the code in the else block will get executed only when all the fruits are iterated
# list iteration is exhausted (no more item to iterate)
for fruit in fruits:
    print(fruit)
    # since we added this condition now when it sees mango 
    # jumps out of the loop (list iteration is not exhausted)
    # the code in the else block not executeds
    if (fruit == "mango"): break
else:
    print("All fruits printed")

# Code in the else block gets executed only when the
# condition fails
multiplicant = 9
multiplier = 1
while (multiplier <= 12):
    print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)
    multiplier += 1
    # since we added this condition now when it sees 11 
    # jumps out of the loop (condition not fail yet 11 <= 12 true)
    # the code in the else block not executeds    
    if multiplier == 11: break
else:
    print("Multiplication table done")

multiplicant = 10
multipliers = range(1,13)
for multiplier in multipliers:
    if multiplier % 5 == 0 : continue  #jump back to loop without execute line below

    print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)