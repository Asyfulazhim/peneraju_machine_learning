import numpy as np

num_rolls = int(input("Enter the number of dice rolls\n"))

dice_rolls = []

print("Enter the value of each dice roll")
for _ in range(num_rolls):
    roll = int(input())
    dice_rolls.append(roll)

dice_rolls = np.array(dice_rolls)

count_greater_than_2 = np.sum(dice_rolls > 2)

print("Dice rolls greater than 2")
print(count_greater_than_2)
   