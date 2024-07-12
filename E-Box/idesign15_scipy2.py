import numpy as np
from scipy.stats import linregress  

x_input = input("Enter the values of x separated by spaces: ")
y_input = input("Enter the values of y separated by spaces: ")

x = [float(num) for num in x_input.split()]
y = [float(num) for num in y_input.split()]

slope, intercept, rvalue, pvalue, se = linregress(x, y)

print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {rvalue**2}")
print(f"p-value: {pvalue}")
print(f"Standard error: {se}")
