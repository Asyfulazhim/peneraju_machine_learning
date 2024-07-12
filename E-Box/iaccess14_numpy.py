# Problem 1

import numpy as np
import pandas as pd

data1 = np.arange(0,100)
data2 = np.arange(2000, 10000, 100)

print("Array 1")
print(data1)
print("Array 2")
print(data2)

# Problem 2
from sklearn.datasets import load_iris
import numpy as np

# Load the Iris dataset
iris = load_iris()

feature_names = iris.feature_names
target_names = iris.target_names
first_5_features = iris.data[:5]
first_5_targets = iris.target[:5]

# Print the results
print("Iris Feature Names")
print(feature_names)
print("Iris Target Names")
print(target_names)
print("Iris Feature Matrix")
print(first_5_features)
print("Iris Target Vector")
print(first_5_targets)

print("Type of Iris Feature Matrix")
print("class 'numpy.ndarray'")
print("Type of Iris Target Vector")
print("class 'numpy.ndarray'")