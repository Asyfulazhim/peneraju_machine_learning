# Problem 7
# Write a python function that takes 2 parameters lower and upper (range). Let the function returns pairs of amicable numbers in that range.
# Two different numbers are called amicable numbers if the sum of the proper divisors of each is equal to the other number. 
# For example 220 and 284 are amicable numbers.
# For example if we call that function: amicableNumbers(1, 1000)
# The function must return: [220, 284]
# Why they are amicable numbers ?
# Sum of proper divisors of 220 = 1+2+4+5+10+11+20+22+44+55+110 = 284
# Sum of proper divisors of 284 = 1+2+4+71+142 = 220
def sumOfDivisors(n):
    # Calculate the sum of proper divisors of a number
    sum = 1  # 1 is a proper divisor
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += i
            if i!= n // i:  # avoid duplicates
                sum += n // i
    return sum

def amicableNumbers(lower, upper):
    # Find amicable numbers in a given range.
    amicableNumbers = []
    for i in range(lower, upper):
        sumOfDivisors_i = sumOfDivisors(i)
        if sumOfDivisors_i > i and sumOfDivisors_i < upper:
            sumOfDivisors_j = sumOfDivisors(sumOfDivisors_i)
            if sumOfDivisors_j == i:
                if i not in amicableNumbers and sumOfDivisors_i not in amicableNumbers:
                    amicableNumbers.append(i)
                    amicableNumbers.append(sumOfDivisors_i)
    return amicableNumbers

# Take input from user
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

result = amicableNumbers(lower, upper)
print("Amicable numbers in the range:", result)
