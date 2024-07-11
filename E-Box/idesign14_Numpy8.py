import numpy as np

# Get the size of the first array from the user
size1 = int(input("Enter the size of 1st array\n"))

# Get the elements of the first array from the user
print("Enter the elements of first array")
array1 = []
for _ in range(size1):
    element = float(input())
    array1.append(element)

# Convert the list to a numpy array
array1 = np.array(array1)

# Get the size of the second array from the user
size2 = int(input("Enter the size of 2nd array\n"))

# Get the elements of the second array from the user
print("Enter the elements of second array")
array2 = []
for _ in range(size2):
    element = float(input())
    array2.append(element)

# Convert the list to a numpy array
array2 = np.array(array2)

# Perform set operations using numpy functions
union_array = np.union1d(array1, array2)
intersection_array = np.intersect1d(array1, array2)
difference_array = np.setdiff1d(array1, array2)

# Print the results
print("Union Array")
print(union_array)
print("Intersection Array")
print(intersection_array)
print("Difference Array")
print(difference_array)
