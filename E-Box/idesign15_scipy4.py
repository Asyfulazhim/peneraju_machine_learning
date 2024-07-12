import numpy as np
from scipy.integrate import dblquad  

func = input("Enter the function to be integrated in terms of x and y:\n")
x_low = int(input("Enter the lower limit for x:\n"))
x_upper = int(input("Enter the upper limit for x:\n"))
y_low = int(input("Enter the lower limit for y:\n"))
y_upper = int(input("Enter the upper limit for y:\n"))

# y_low = lambda x: y_low
# y_upper = lambda x: y_upper

integral = lambda y, x: eval(func)
# formula /  syntax
# area = dblquad(lambda x, y: func, x_low, x_upper, lambda x: x_low, lambda x: x_upper)

result, error = dblquad(integral, x_low, x_upper,lambda x: y_low, lambda x: y_upper)

print(f"Result of dblquad integration: {result}")
print(f"Error estimate: {error}")