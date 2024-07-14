import math
import numpy as np
from scipy import stats

def logistic_regression(x):
    return 1 / (1 + math.exp(-x))

x = float(input("Enter the value of x\n"))
result = logistic_regression(x)
print(round(result, 2))