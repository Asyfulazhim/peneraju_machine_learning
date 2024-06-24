# tuple is nothing but read-only list
# tuple is immutable
# tuple is defined using parentheses()
# tuple is faster than list


x = (10,20,30,40,50)
print(x)
print(type(x))

# selection and indexing
# refer to variableparttwo
print(x[0]) # 10

# use count
# it is not midifiable
# do not have append, insert, remove
fruits = ("apple", "orange", "mango", "apple")
print(fruits.count("apple"))

# can delete entire tuple using
del fruits
#print(fruits) # error

# why we use tuple?
# 1) take less space
# 2) faster than list
# 3) immutable
# 4) use in dictionary keys
# 5) use in set
# 6) use in function return type

# example use in function return type
def returnFruit():
    return "apple", "orange"
print(returnFruit()) # returns tuple
print(type(returnFruit())) # returns tuple

def total(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result

print(total(10,20,30,40,50)) 

# how to convert list to tuple
# you pass list to the tuple class and it will return tuple object
x = [10,20,30,40,50]
x =tuple(x) # convert list to tuple
print(x)

# one last feature in list
# list can auto explode
# explode means create 1 variable fir every item in the list
# if you have list of list
# you can use * to explode it
fruits = ["apple", "orange", "mango"]
fruits01 = fruits[0]

# however in python you no need to explode manually
fruit01, fruit02, fruit03 = fruits
#assigning multiple items in the list to the multiple variable
print(fruit01)

# we also can use explode in tuple
fruits = ("apple", "orange", "mango")
fruits01 = fruits[0]
fruit01, fruit02, fruit03 = fruits
print(fruit01)

# there is a problem highlight in tuple
x = (10)
# python really confused whether it is tuple or expression
# python give priority for expression than tuple
# so it will be considered as expression
print(type(x)) # returns int

# to ensure the data is in tuple format please addd extra comma
x = (10,)
print(type(x)) # returns tuple