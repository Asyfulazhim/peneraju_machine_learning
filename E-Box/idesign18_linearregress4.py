import numpy as np

x = [float(i) for i in input().split(' ')]
y = [float(i) for i in input().split(' ')]

# Calculate correlation coefficient
correlation_coefficient = np.corrcoef(x, y)[0, 1]

# Print result
if correlation_coefficient % 1!=0:
    print(f"{correlation_coefficient:.2f}") 
else:
    print(f"{correlation_coefficient}") 