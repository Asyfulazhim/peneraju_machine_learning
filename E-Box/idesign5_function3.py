# Write a program to find the GCD and LCM of two numbers using functions.

# Python Function Specification:
# def GCD (n1,n2):
# def LCM (n1,n2):
# Function should return the output.

# INPUT AND OUTPUT FORMAT:
# Input consists of two integers corresponding to two values.
# Output consists of two integers corresponding to GCD and LCM of the two numbers.

# SAMPLE INPUT AND OUTPUT:
# Enter two integers:
# 3
# 9
# Greatest common divisor of 3 and 9 = 3
# Least common multiple of 3 and 9 = 9

def GCD (n1,n2):
    while n2 != 0:
        n1,n2 = n2, n1 % n2
    return int(n1)

def LCM (n1,n2):
    return abs(n1 * n2) // GCD(n1,n2)

print("Enter two integers:")
n1 = int(input())
n2 = int(input())
gcd = GCD(n1,n2)
lcm = LCM(n1,n2)
print(f"Greatest common divisor of {n1} and {n2} = {gcd}")
print(f"Least common multiple of {n1} and {n2} = {lcm}") 