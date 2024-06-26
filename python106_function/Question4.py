# Problem 4
# Write a function that inputs a number and returns the product of digits of that number.

def digitproduct(num):
  total = 1
  while num != 0:
    r = num % 10
    total *= r
    num //= 10**1
  return total

y = int(input("Enter any number: "))
print(f"Answer: {digitproduct(y)}")