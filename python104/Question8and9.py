# Problem 8
# Write a python program that takes few numbers as command line argument. Use a loop to display all elements. 
# Use another loop to display all elements in the even position. Use another loop to display all elements in the odd position.

import sys

numbers = sys.argv[1:]

print("All elements:")
for num in numbers:
    print(num, end=' ')
print()

print("Elements in even positions:")
for i in range(0, len(numbers), 2):
    print(numbers[i], end=' ')
print()

print("Elements in odd positions:")
for i in range(1, len(numbers), 2):
    print(numbers[i], end=' ')
print()


# Problem 9
# Write a python program that takes few numbers as command line argument. Find the average of those numbers

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