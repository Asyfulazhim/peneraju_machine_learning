# Problem 2
# Write a simple python function that returns twin primes less than 1000. 
# If two consecutive odd numbers are both prime then they are known as twin primes.
# Pairs of primes that differ by 2. For example, 3 and 5, 5 and 7, 11 and 13, and 17 and 19 are twin primes.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def twin_prime(t):
    twin_primes = []
    for i in range(2, t):
        if is_prime(i) and is_prime(i + 2):
            twin_primes.append((i, i + 2))
    return twin_primes
        
twin_primes = twin_prime(1000)
for prime in twin_primes:
    print(f"{prime[0]} and {prime[1]}")


# Problem 3
# Write a simple python function that takes a number as parameter 
# and returns the prime factors of that number. Prime Factorization is finding which prime numbers multiply together to make the original number.
# Example: prime factors of 56 - 2, 2, 2, 7

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def prime_factor(t):
    prime_factors = []
    i = 2
    while i <= t:
        if t % i == 0 and is_prime(i):
            t //= i
            prime_factors.append(i)
            if t // i == 1:break
        else:
            i += 1
    return prime_factors

n = int(input("Enter a number:"))
print(f"{n} - ", end = " ")
prime_factors = prime_factor(n)
for factor in prime_factors:
    print(f"{factor}")