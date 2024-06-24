'''
#Question 1

x = int(input("Enter any integer number: "))
if(x % 2 == 1):
  print(x, " is an odd number")
else:
  print(x, "is an even number")
'''

'''
#Question2
score = int(input("Enter your score: "))
if (score >= 90):
  print("Your score = A")
elif (score < 90 and score >=  80):
  print("Your score = B")
elif (score < 80 and score >= 70):
  print("Your score = C")
elif (score < 70 and score >= 60):
  print("Your score = D")
else:
  print("Your score = F")
'''

'''
#Q3

year = int(input("Please enter any year: "))
if (year % 4 == 0):
  print(year, "is a leap year")
else:
  print(year, "is not a leap year")
'''

'''
#Q4
x = int(input("Enter first integer number: "))
y = int(input("Enter second integer number: "))
z = int(input("Enter third integer number: "))

if (x > y and x > z):
  print(x, "is the largest number")
elif (y > x and y > z):
  print(y, "is the largest number")
else:
  print(z, "is the largest number")
'''

'''
#Q5
char = str(input("Enter any single character: "))

if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' ):
  print(char, "is a vowel")
else:
  print(char, "is a consonent")
'''

'''
#Q6
height = float(input("Your height: "))
weight = float(input("Your weight: "))
bmi = weight / (height ** 2)
print("BMI = ",bmi)

if (bmi < 18.5):
  print("Category: Underweight")
elif (bmi >= 18.5 and bmi < 24.9):
  print("Category: Normal weight")
elif (bmi >= 25 and bmi < 29.9):
  print("Category: Normal weight")
else: 
  print("Category: Obesity")
'''

'''
#Question 7
length1 = float(input("First length: "))
length2 = float(input("Second length: "))
length3 = float(input("Third length: "))

if (length1 == length2 and length1 == length3):
  print("This is Equilateral triangle")
elif (length1 == length2 or length2 == length3 or length3 == length1):
  print("This is Isoscelesl triangle")
else:
  print("This is Equilateral triangle")
'''
'''
#Question 8

amount = int(input("Enter amount: "))

if (amount % 10 == 0):
    fifty = amount // 50    
    amount %= 50
    twenty = amount // 20
    amount %= 20
    ten = amount // 10

    print(fifty, "x 50 dolar, ", twenty, "x 20 dollar, ", ten, "x 10 dollar")

else:
    print("Invalid amount!!! Please enter number with multiple 10")
''' 

#Question 9
a0 = int(input("Enter any integer: "))

if (a0 // 10 == 0):
    print(a0, "is Adam number")
elif(a0 // 100 == 0):
    result = a0 % 10
    a1 = a0 // 10
    result = (result * 10) + (a1 % 10)

    ad0 = result ** 2
    a0square = a0 ** 2

    result1 = ad0 % 10
    ad1 = ad0 // 10
    result1 = (result1 * 10) + (ad1 % 10)
    ad2 = ad1 // 10
    result1 = (result1 * 10) + (ad2 % 10)
    if(ad0 // 1000 != 0):
        ad3 = ad2 // 10
        result1 = (result1 * 10) + (ad3 % 10)

else:
    result = a0 % 10
    a1 = a0 // 10
    result = (result * 10) + (a1 % 10)
    a2 = a1 // 10
    result = (result * 10) + (a2 % 10)

    ad0 = result ** 2
    a0square = a0 ** 2

    result1 = ad0 % 10
    ad1 = ad0 // 10
    result1 = (result1 * 10) + (ad1 % 10)
    ad2 = ad1 // 10
    result1 = (result1 * 10) + (ad2 % 10)
    ad3 = ad2 // 10
    result1 = (result1 * 10) + (ad3 % 10)
    ad4 = ad3 // 10
    result1 = (result1 * 10) + (ad4 % 10)
    if(ad0 // 100000 != 0):
        ad5 = ad4 // 10
        result1 = (result1 * 10) + (ad5 % 10)

print("Square of", a0, "is", a0square)
print("Reverse of", a0, "is", result,)
print("Square of", result,"is", ad0)
print("")

if(a0square == result1):
    print("Therefore,",a0, "is Adam number")
else:
    print("Therefore",a0, "is not Adam number")

'''
#Question 10
print("disclaimer: this system only can process up to 4 digit numbers")
a0 = int(input("Enter any number: "))

if (a0 // 10 == 0):
    digit = 1
    result = a0
    print(result, "is Armstrong number")
elif (a0 // 100 == 0):
    digit = 2

    r1 = a0 % 10
    a1 = a0 // 10
    result = r1 ** digit

    r2 = a1 % 10
    result = result + (r2 ** digit)
    print(result)

    if(a0 == result):
        print(a0, "is Armstrong number")
    else:
        print(a0, "is not Armstrong number") 

elif (a0 // 1000 == 0):
    digit = 3
    
    r1 = a0 % 10
    a1 = a0 // 10
    result = r1 ** digit

    r2 = a1 % 10
    a2 = a1 // 10
    result = result + (r2 ** digit)

    r3 = a2 % 10
    result = result + (r3 ** digit)

    if(a0 == result):
        print(a0, "is Armstrong number")
    else:
        print(a0, "is not Armstrong number") 
    
elif (a0 // 10000 == 0):
    digit = 4
    
    r1 = a0 % 10
    a1 = a0 // 10
    result = r1 ** digit

    r2 = a1 % 10
    a2 = a1 // 10
    result = result + (r2 ** digit)

    r3 = a2 % 10
    a3 = a2 // 10
    result = result + (r3 ** digit)

    r4 = a3 % 10
    result = result + (r4 ** digit)

    if(a0 == result):
        print(a0, "is Armstrong number")
    else:
        print(a0, "is not Armstrong number") 

else (a0 // 10000000 == 0):
    print(a0, "is over the limit") 
'''

'''
r1 = value % 10
a1 = value // 10
result = (r1**r1) 
print(result, r1, a1)

r2 = a1 % 10
a2 = a1 // 10
result = result + (r2 ** r1)
print(result, r2, a2)

r3 = a2 % 10
a3 = a2 // 10
result = result + (r3 ** r1)
print(result, r3, a3)

if (value == result):
    print(value, "is an armstrong number")
else:
    print(value, "is not armstrong number")
'''
