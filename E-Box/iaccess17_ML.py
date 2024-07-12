'''

Find mean, median, standard deviation, and mode

Write a python program that takes a list of numbers as input and calculates the mean, median, standard deviation, and mode. Scikit-learn and scipy libraries are used for some calculations.

Input Format:
The input consists of n, the number of elements in the list, followed by n integers. The integers correspond to the elements in the list.

Output Format:
The program outputs the mean, median, standard deviation, and mode.

Sample Input and Output:
Enter the number of elements:
5
Enter the elements:
3 5 7 6 5
Mean: 5.2
Median: 5.0
Standard Deviation: 1.3266
Mode: 5
'''
import numpy as np
import scipy.stats as stats

n = int(input("Enter the number of elements:\n"))
elements = list(map(int, input("Enter the elements:").split()))
data = np.array(elements)

mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
mode = stats.mode(data)
mode = stats.mode(data)[0][0]

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev:.4f}")
print(f"Mode: {mode}")

# Problem 2
import numpy as np 
from sklearn.metrics import mean_squared_error 

x = input("Enter actual values\n")
y = input("Enter predicted values\n")

actual_value = list(map(float, x.split(",")))
predict_value = list(map(float, y.split(",")))

print("List of Actual Values")
print(actual_value)
print("List of Predicted Values")
print(predict_value)
print("MSE")

MSE = mean_squared_error(actual_value,predict_value) 
print(round(MSE, 2))