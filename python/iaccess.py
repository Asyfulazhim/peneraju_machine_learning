# chapter 3
a = int(input())
b = int(input())
prime = []

for num in range(a, b+1):
    if num > 1:
        is_prime = True
        for i in range(2, num):   
            if num % i == 0: 
                is_prime = False
                break
        if is_prime:
            prime.append(num)

for num in prime:
    print(num, end=" ")

# Chapter 4