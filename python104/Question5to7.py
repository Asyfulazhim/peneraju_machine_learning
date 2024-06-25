# Problem 5
# Write a program to print the following pattern using a loop.

# o
# oo
# ooo
# oooo
# ooooo

for num in range (1,6):
   print("o" * num)

# Problem 6
# Write a program to print the following pattern using a loop

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for num in range(1,6):
  for n in range(1,num+1):
    print(n, end='')
  print()

# Problem 7
# Get a number as input and calculate the sum of all numbers from 1 to the given number.

n = int(input("Enter any number: "))
result = 0
for num in range(1,n+1):
  result = result + num
print(f"Sum of all numbers from 1 to {n} = {result}")