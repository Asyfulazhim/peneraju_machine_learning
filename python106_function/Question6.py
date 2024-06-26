# perfect number

def get_divisors(n):
    """Return a list of divisors of n"""
    divisors = []
    half = int(n / 2)
    for i in range(1, half + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def is_perfect(n):
    """Return True if n is a perfect number, False otherwise"""
    divisors = get_divisors(n)
    return sum(divisors) == n

def find_perfect_numbers(pf):
    """Find the first pf perfect numbers"""
    perfect = []
    count = 0
    for num in range(1, 10**6):
        if is_perfect(num):
            perfect.append(num)
            count += 1
        if count == pf:
            break
    return perfect

PF = 4
perfect_numbers = find_perfect_numbers(PF)
print(f"Perfect Numbers: {perfect_numbers}")