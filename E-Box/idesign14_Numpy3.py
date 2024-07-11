import numpy as np

n = int(input("Enter the size of the list\n"))
print("Enter the elements in the list")
element = [input() for _ in range(n)]

df = np.array(element)
print("class 'numpy.ndarray'")
print(df.astype(int))