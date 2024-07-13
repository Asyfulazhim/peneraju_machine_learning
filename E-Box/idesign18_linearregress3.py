import numpy as np 

nums = input().split(" ")
numbers = list(map(float, nums))

mean_x = np.mean(numbers)
print(mean_x)
