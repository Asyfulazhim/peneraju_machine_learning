'''
Exercise 1: Basic Arithmetic Operations

Write a Python program that does the following:

Prompts the user to enter two numbers. Stores these numbers in two variables. 
Performs and prints the results of addition, subtraction, multiplication, and 
division of these two numbers.


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
'''

'''
Exercise 2: Temperature Converter

Write a Python program that:

Prompts the user to enter a temperature in Celsius. Converts the temperature to Fahrenheit. 
Prints the temperature in Fahrenheit. 
(Hint: The formula to convert Celsius to Fahrenheit is: F = C * 9/5 + 32)

tempCelcius = float(input("Enter the temperature in Celcius: "))
tempFahrenheit = float(tempCelcius * (9/5)) + 32
print("Temperature in Fahrenheit: ", tempFahrenheit)
'''
'''
Exercise 3: Area and Perimeter of a Rectangle

Write a Python program that:

Prompts the user to enter the length and width of a rectangle. 
Calculates the area and perimeter of the rectangle. Prints the area and perimeter.

length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area = ", area)
'''
'''
Exercise 4: Simple Interest Calculator

Write a Python program that:

Prompts the user to enter the principal amount, rate of interest, and time in years. 
Calculates the simple interest. Prints the simple interest. 
(Hint: The formula to calculate simple interest is: SI = (P * R * T) / 100)

P = float(input("Enter the pricipal amount: "))
R = float(input("Enter rate of interest: "))
T = float(input("Enter time in years: "))

SI = ((P * R * T) / 100)
print("Simple interest = ", SI)
'''

'''
Exercise 5: Swapping Two Variables

Write a Python program that:

Prompts the user to enter two numbers. Swaps the values of the two variables. 
Prints the values before and after swapping.

x = int(input("Enter first whole number (x): "))
y = int(input("Enter second whole number (y): "))

print("before swapping: ", x, y)

x = x + y
y = x - y
x = x - y

print("After swapping: ", x, y)
'''

'''
Exercise 6: Square and Cube

Write a Python program that:

Prompts the user to enter a number. Calculates the square and cube of the number. 
Prints the square and cube.

x = float(input("Enter any number: "))
square = x ** 2
cube = x ** 3
print("Square = ", square)
print("Cube: ", cube)
'''

'''
Exercise 7: Calculate BMI

Write a Python program that:

Prompts the user to enter their weight in kilograms and height in meters. 
Calculates the Body Mass Index (BMI). Prints the BMI. 
(Hint: The formula to calculate BMI is: BMI = weight / (height * height))

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height * height)
print("Your BMI = ", bmi)
'''

'''
Exercise 8: Compound Interest Calculator

Write a Python program that:

Prompts the user to enter the principal amount, rate of interest, 
time in years, and number of times interest is compounded per year. 
Calculates the compound interest. Prints the compound interest.

(Hint: The formula to calculate compound interest is: 
 A=P(1+R/100n)nt where A is the amount, P is the principal amount, 
 R is the annual interest rate, t is the time the money is invested for, 
 and n is the number of times interest is compounded per year)

principal = float(input("Enter principal amount: "))
interestRate = float(input("Enter rate of interest: "))
years = float(input("Enter times in years: "))
timecompoundInterest = float(input("Enter number of times interest is compounded per year: "))

P = principal
R = interestRate
t = years
n = timecompoundInterest

A = P * ((1+R)/(100 * n)) * (n * t)
print("Compound Interest: ", A)

x0 = 1011

x1 = x0 // 10   #101
remainder0 = x0 % 10    #1
result = (2**0) * remainder0    #1

x2 = x1 // 10   #10
remainder1 = x1 % 10    #1
result = ((2**1) * remainder1) + result #2 + 1 = 3

x3 = x2 // 10   #1
remainder2 = x2 % 10    #0
result = ((2**2) * remainder2) + result #3

x4 = x3 // 10   #0
remainder3 = x3 % 10    #1
result = ((2**3) * remainder3) + result #8 + 3 = 1

print(x0)
print("Decimal Expression: ", result)
'''

string_number = str(input("Enter multiple number separated by comma: "))
numbers = list(map(int,string_number.split(",")))
print(len(numbers))

index1 = 0
samenumber = 0
for num in numbers:
    index2 = 0
    #print("num: ", num)
    for n in numbers:
        print("n: ", n)
        if(index1 != index2):
            if (num == n):
                print ("Same number detected!")
                samenumber += 1
                break
        index2 += 1
    if(samenumber == 1):break
    index1 += 1
else:
    print("All numbers are different")

