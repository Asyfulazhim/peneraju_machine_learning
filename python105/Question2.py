# Problem 2 Collatz Sequence:

def number (num):
  if num % 2 == 0:
    r = num // 2
    print(r, end=" ")
    return r
  elif num % 2 == 1:
    r = (3 * num) + 1
    print(r, end=" ")
    return r

n = int(input())
print(n, end = " ")
while n != 1:
  n = number (n)