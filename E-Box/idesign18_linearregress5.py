import numpy as np
from scipy import stats

x = [float(num) for num in input().split(' ')]
y = [float(num) for num in input().split(' ')]

x_mean = np.mean(x)
y_mean = np.mean(y)
print(f"Mean of x = {x_mean}")
print(f"Mean of y = {y_mean}")

x_std = np.std(x)
y_std = np.std(y)
print(f"SD of x = {x_std:.3f}")
print(f"SD of y = {y_std:.3f}")

correlation = np.corrcoef(x,y)[0,1]
print(f"Correlation of x and y = {correlation:.3f}")

slope, intercept, r, p, std_err = stats.linregress(x, y)
print(f"Scope = {slope:.3f}")
print(f"Intercept = {intercept:.3f}")
