# Problem 6 Perfect Number: Write a program that generates 10 perfect numbers

import sympy

primes = [p for p in sympy.primerange(2, 10**6)]

PF = 4
count = 0
divisors = []
perfect = []

#print("Prime numbers up to 100:", primes)

for num1 in range(1,10**6):
  half = int(num1 / 2)
  if(num1 in primes):continue
  for num2 in range(1,half + 1):
    if(num1 % num2 == 0):
      divisors.append(num2)
  total = sum(divisors)
  if (total == num1):
    perfect.append(num1)
    count += 1
  divisors.clear()
  if count == PF: break
print(f"Perfect Numbers: {perfect}")