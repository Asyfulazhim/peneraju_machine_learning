# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three, print "Fizz" instead of the number, 
# and for the multiples of five, print "Buzz". For numbers which 
# are multiples of both three and five, print "FizzBuzz".

count = 0
for num in range(1,101):
  if(num % 3 == 0 and num % 5 == 0):
    print("FizzBuzz", end=" ")
  elif(num % 3 == 0 and num % 5 != 0):
    print("Fizz", end=" ")
  elif(num % 3 != 0 and num % 5 == 0):
    print("Buzz", end=" ")
  else:
    print(num, end=" ")
  count += 1

  if count==10:
    print()
    count = 0
