# prob 1
cov = float(input())
var_x = float(input())
var_y = float(input())

# Calculate correlation coefficient (r)
r = cov / ((var_x ** 0.5) * (var_y ** 0.5))

print(f"{r:.3f}")

# prob 2
import numpy as np

x = [int(i) for i in input().split(' ')]

Sx = np.std(x)
print(round(Sx, 2))