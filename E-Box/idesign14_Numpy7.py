import numpy as np

size = int(input("Enter the size of 1-D array\n"))

one_darray = np.array(range(size))

print("1-D Array")
print(one_darray)

m = int(input("Enter m value\n"))
n = int(input("Enter n value\n"))

# Check if the array can be reshaped to m rows and n columns
if size != m * n:
    print("Error: The size of the 1-D array does not match m * n")
else:
    two_darray = one_darray.reshape(m, n)
    
    print("2-D Array")
    print(two_darray)
   