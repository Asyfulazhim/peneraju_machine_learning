# import numpy as np
# from scipy.integrate import dblquad  

# def user_defined_function(x, y, func):
#     return eval(func)

# func = input("Enter the function to be integrated in terms of x and y:\n")
# x_low = int(input("Enter the lower limit for x:\n"))
# x_upper = int(input("Enter the upper limit for x:\n"))
# y_low = int(input("Enter the lower limit for y:\n"))
# y_upper = int(input("Enter the upper limit for y:\n"))

# integral = lambda x, y: user_defined_function(x,y,func)

# # formula /  syntax
# # area = dblquad(lambda x, y: func, y_low, y_upper, lambda x: x_low, lambda x: x_upper)

# result, error = dblquad(integral, y_low, y_upper, lambda x: x_low, lambda x: x_upper)

# print(f"Result of dblquad integration: {result}")
# print(f"Error estimate: {error}")
