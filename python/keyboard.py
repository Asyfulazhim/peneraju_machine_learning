# python has a built in function called input
# the input function takes a single parameter (caption / question)
# Input function will display the caption 
# and wait for the user input
# The user will provide the input and press enter key
# what ever the user provide will be stored in a variable
firstnumber = input("Please key in the first number: ")
print(firstnumber)
# the input is always return value of type string
print(type(firstnumber))

secondnumber = input("Please key in the second number: ")
print(firstnumber + secondnumber) # string concatenation
print(int(firstnumber) + int(secondnumber)) # addition

numbers = input("Enter the numbers to do Total: ")
numberlist = numbers.split(",")
print(numberlist)
total = 0
for number in numberlist:
    # int function trim the string value
    # remove the spaces in the string and then convert
    # string to integer
    total = total + int(number)
print(total)