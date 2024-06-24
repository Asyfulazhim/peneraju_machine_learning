#Arithmetic Operators
x = 7
y = 2
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)

print("Quotient:", x//y)
print("Remainder:", x % y)

print("Exponent: ", 10 ** 3)
print("What is the maximum number in a 64 bit env: ", (2 ** 64)-1)

#Comparison operator
myheight = 5.2
yourheight = 5.3
mysisterheight = 5.2

#Let us create True Statement
print(yourheight > myheight)    #greater than   
print(myheight == mysisterheight)   #equals to
print(mysisterheight < yourheight)  #lower than
print(myheight != yourheight)   #not equal to

print(yourheight >= myheight)   #greater than or equal to
print(myheight >= mysisterheight)   

print(myheight <= yourheight)   #lower than or equal to
print(mysisterheight <= myheight)

a = 21
b = 14
c = 7

print(a > b and a > c)  #a is the greatest number
print(c < a and c < b)  # c is smallest number
print((b > c and b < a) or (b > a and b < c))

#Negation operator
print(not (a > c))  #False
print(not (a < c))  #True

# Truth table
print("XOR", (a > b)^(a > c))  # XOR



