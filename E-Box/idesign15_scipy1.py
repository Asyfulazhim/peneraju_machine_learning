'''
Write a Python program to explore the functionalities of SciPy's Special Function package. Write a program to demonstrate the usage of various exponential and trigonometric functions available in SciPy, Use exp10(), sindg(), and cosdg().

Input and Output format:
The first line of input contains the exponent value for exponent calculation. 
The second line of input contains the angle in degrees for sine and cosine calculation. 

Sample Input and Output:
Enter the exponent value:
3
10 raised to the power of 3 : 1000.0
Enter the angle in degrees:
90
Sine of 90.0 degrees: 1.0
Cosine of 90.0 degrees: -0.0
'''

import numpy as np
import scipy.special as sp

exponent = int(input("Enter the exponent value:\n"))
exp_result = sp.exp10(exponent)
print(f"10 raised to the power of {exponent} : {exp_result}")

angle = float(input("Enter the angle in degrees:\n"))
sin_result = sp.sindg(angle)
cos_result = sp.cosdg(angle)

print(f"Sine of {angle} degrees: {sin_result}")
print(f"Cosine of {angle} degrees: {cos_result}")