#Problem 5 Number Guessing Game:

import random
rand_Num = random.randint(1,100)
print(rand_Num)

user_Num = 0

while rand_Num != user_Num:
  user_Num = int(input("Guess the number: "))
else:
  print("The answer is correct!")