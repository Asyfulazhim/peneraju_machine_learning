import math

# Read input vectors
vector1 = list(map(float, input("Enter the first vector\n").split()))
vector2 = list(map(float, input("Enter the second vector\n").split()))

# Calculate Euclidean distance
distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(vector1, vector2)]))

# Print the result with 5 decimal precision
print("{:.5f}".format(distance))