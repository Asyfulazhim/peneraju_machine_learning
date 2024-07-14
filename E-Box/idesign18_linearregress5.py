import numpy as np
from scipy import stats

x = [float(num) for num in input().split(' ')]
y = [float(num) for num in input().split(' ')]

Mx = np.mean(x)
My = np.mean(y)
print(f"Mean of x = {Mx}")
print(f"Mean of y = {My}")

Sx = np.std(x)
Sy = np.std(y)
print(f"SD of x = {round(Sx,3)}")
print(f"SD of y = {round(Sy,3)}")

r = np.corrcoef(x,y)[0,1]
print(f"Correlation of x and y = {round(r,3)}")

# Calculate slope (b)
b = r * (Sy / Sx)

# Calculate intercept (A)
a = My - b * Mx

print(f"Scope = {round(b,3)}")
print(f"Intercept = {round(a,3)}")
