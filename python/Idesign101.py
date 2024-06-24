'''
# Question 2
print("Enter your name")
name = input("")
print("Hello", name ,"! Welcome to Amphi Event Management System")
'''

'''
# Question 3
print("Enter branding expenses")
brandingExpenses = int(input(""))
print("Enter travel expenses")
travelExpenses = int(input(""))
print("Enter food expenses")
foodExpenses = int(input(""))
print("Enter logistics expenses")
logisticsExpenses = int(input(""))

totalExpenses = float(brandingExpenses + travelExpenses + foodExpenses + logisticsExpenses)
print(f"Total expenses : {totalExpenses:.2f}")

brandingPercentage = float(brandingExpenses / totalExpenses) * 100
travelPercentage = float(travelExpenses / totalExpenses) * 100
foodPercentage = float(foodExpenses/ totalExpenses) * 100
logisticsPercentage = float(logisticsExpenses / totalExpenses) * 100


print(f"Branding expenses percentage : {brandingPercentage:.2f}%")
print(f"Travel expenses percentage : {travelPercentage:.2f}%")
print(f"Food expenses percentage : {foodPercentage:.2f}%")
print(f"Logistics expenses percentage : {logisticsPercentage:.2f}%")
'''
'''
#Question 4

print("Enter the value of X")
x = int(input(""))
print("Enter the value of Y")
y = int(input(""))

c = (y - (5*x)) / 13
a = c + x
s = 2 * c

print("Number of children tickets sold :", int(c))
print("Number of adult tickets sold :",int(a))
print("Number of senior tickets sold :", int(s))
'''
'''
# Question 5

print("Enter the side in cm of a square tile")
length = int(input(""))
print("Enter the number of square tiles available")
inputTile = int(input(""))

increment = 1
numtile = 1
increment += 2
if (inputTile >= (numtile + increment)):
    numtile += increment
    increment += 2
    if(inputTile >= (numtile + increment)):
        numtile += increment
        increment += 2
        if(inputTile >= (numtile + increment)):
            numtile += increment

totalArea = int((numtile ** (1/2)) * length) ** 2
print(f"Area of the largest possible square is {totalArea}sqm")
'''
'''
# Question 6

totalSalary = int(input("Enter the total salary paid\n"))
end = (totalSalary - 800) // 130
day = end + 10

print(f"Number of weekday hours is {day}")
print(f"Number of weekend hours is {end}")
'''
'''
# Question 7
a = input()
al = a.split(" ")
print(a)
print(al)
'''
if True or True:
    if False and True or False:
        print('A')
    elif False and False or True and True:
        print('B')
    else:
        print('C')
else:
    print('D')
