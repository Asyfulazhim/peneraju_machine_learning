'''
Correlation coefficient - Scattered Data

To find the correlation coefficient for scattered data. 

Input Format
First line of input in an integer n that corresponds to number of points
Next n line consists of points in the format x,y 

Output Format 
Output is a float value with two 2 precision that corresponds to the correlation coefficient of scattered data. 

Sample Input 
3 
12,6 
13,32 
1,7 

Sample Output 
Correlation Coefficient: 0.54
'''
import numpy as np

# Read input
n = int(input())
points = [input().split(',') for _ in range(n)]
x = [float(point[0]) for point in points]
y = [float(point[1]) for point in points]

# Calculate correlation coefficient
correlation_coefficient = np.corrcoef(x, y)[0, 1]

# Print result
print(f"Correlation Coefficient: {correlation_coefficient:.2f}")