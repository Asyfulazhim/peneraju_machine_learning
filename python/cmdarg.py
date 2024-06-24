# When we call python to executed our program we can pass values to 
# our program in the command line which is also called command line arguments
# these arguments are seperated by space
# all these arguments inside the list are string type
# Remember the arguments for function is seperated by comma

# sys.argv give us a list, which contains all the command line arguments 
# passed to python
# in the list you can see the item at position 0 is program name itself
import sys

cmdarguments = sys.argv # we are using . (dot) operator to access
# the variable which is inside the module sys
print(cmdarguments)

# find the total of all the arguments
# if we know the total number of arguments then we can hardcode it
# total = int(cmdarguments[1]) + int(cmdarguments[2])

# In this case we have to use loops (since we do not know the total number of arguments)
'''
total = 0
for number in cmdarguments[1:]:
    total = total + int(number)
print(total)
'''
'''
import sys

# Get the command line arguments
numbers = sys.argv[1:]

# Display all elements
print("All elements:")
for num in numbers:
    print(num, end=' ')
print()

# Display elements in even positions
print("Elements in even positions:")
for i in range(0, len(numbers), 2):
    print(numbers[i], end=' ')
print()

# Display elements in odd positions
print("Elements in odd positions:")
for i in range(1, len(numbers), 2):
    print(numbers[i], end=' ')
print()
'''
import sys

numbers = sys.argv[1:]
result = 0
print("All element:")
for num in numbers:
  print(num, end=' ')
  result += int(num)
print()

Average = result / len(numbers)
print(f"Average: {Average:.2f} ")

