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
    if n1>n2:
        temp=n1
        n1=n2
        n2=temp
    for i in range(1,n1+1):
        if n1%i==0 and n2%i==0:
            gcd=i
    print(f"Greatest common divisor of {n1} and {n2} = {gcd}")

def LCM (n1,n2):
    if n1>n2:
        temp=n1
        n1=n2
        n2=temp
    for i in range(1,n1+1):
        if n1%i==0 and n2%i==0:
            lcm=n1*i
    print(f"Least common multiple of {n1} and {n2} = {lcm}") 

n1 = int(input())
n2 = int(input())
GCD(n1,n2)
LCM(n1,n2)