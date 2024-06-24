'''
#product is a variable
#"Television" is the string value
#to differentiate the variable from values we use double quote "" 
#or single quote ''
product = "Television"      #string
quantity = 2    #integer
price = 1455.25     #float
available = True    #True/False (boolean value/literal)
#after True/False there is no bracket
#True/False/int/float are keywords

print("Product:", product)
print("Quantity:", quantity)
print("Price:", price)
print("Available:", available)

#type is another built fx that tell us what is the 
#data type of the variable(dinamically assigned by python)
print("product is:",type(product))
print("quantity is:",type(quantity))
print("price is:",type(price))
print("available is:",type(available))

total = quantity*price
print("Total", total)

quantity = "10"
print(type(quantity))
#print(quantity*price)

#type casting
#convert one data type to another
#to convert string to integer in fx int
#to convert string to float in fx float
total = int(quantity) * float(price)
print(total)

x = 100
# i want to know the adress where 100 is
print(x)
#we can use built in fx called id
print(id(x))

y = 100
#however in python, the object 100 is not created first
#python scan first and if the object 100 already exist then
#python will reuse the object instead of re-creating the object

print(id(y))

a = "Heloo"
b = "Heloo"
print(id(a))
print(id(b))
'''

# 7 June 2024

# How to assign more than one value to more than one variable
# in one line of comment
x,y = 101 ,102

#you can also do this
x,y = 101 + 1, 102 + 1
x,y = x + 1, y + 1
print(x,y)

#In some programming language you can assign 
#multiple variable wiyh single value
#x,y = 501  however in pythom this is not allowed

#In other prog language, we call this as initialization
#But in python there is no way for you to create a variable
#without assigning a value
y = 0   #numeric initialization
y = ""  #string initilization / empty string
y = str(None) 

print(type(y))

#function can be treated as variable but it will have side effect. 