# Problem 5
# Write a function that takes a number as parameter. The function finds the 
# proper divisors of that number and then finds the sum of proper divisors. 
# Proper divisors of a number are those numbers by which the number is divisible, except the number itself.
# For example proper divisors of 36 are 1, 2, 3, 4, 6, 9, 18

def proper_divisor(n):
    divisors = []
    for i in range(1, (n//2)+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

num = int(input())
print(f"Proper divisors of {num} are", end=" ")
divisors = proper_divisor(num)
for divisor in divisors:
    print(divisor, end=", ")