# Problem 1
# Print first 10 natural numbers using while loop

num = 1
while (num <= 10):
   print (num, end=' ')
   num += 1

# Problem 2
# Print first 10 prime numbers using for loop

# 1st solution
# no input
count = 1
for num in range(2,100):
   if (count <= 10):
      for i in range(2, num):    # set range between 2 and one number before num
        if num % i == 0: break   # divide the number with all numbers before it number

      else:
        print(num, end=' ')
        count += 1

# 2nd Solution
# user input
n = int(input())
count = 0
number = 2
prime = []

while (count < n):
    isPrime = True
    for num in range(2, number):
        if(number % num == 0 ):
            isPrime = False
            break

    if (isPrime):
        prime.append(number)
        count += 1
    number += 1

for num in prime:
    print(num, end=" ")