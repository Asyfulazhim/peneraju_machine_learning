import numpy as np

a = float(input("Enter the limit\n"))
b = int(input("Enter the number of points\n"))

# Create the numpy array using linspace
array = np.linspace(0, a, b)

# Print the resulting array
print(array)
   