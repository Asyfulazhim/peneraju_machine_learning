# Problem 4 Rock, Paper, Scissors:

import random

C = random.randint(1,3)
print("1 = Rock,  2 = Paper,  3 = Scissor")
U = int(input("Choose one number: "))
print ("Computer choose:", C)
# 1 = Rock
# 2 = Paper
# 3 = Scissor
if (C == U):
  print("Result = DRAW!!")
elif ((U == 1 and C == 3) or (U == 2 and C == 1) or (U == 3 and C == 2)):
  print("YOU WIN!!!")
else:
  print("YOU ARE A LOSERRR!!!")
