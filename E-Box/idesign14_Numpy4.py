from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
data = iris.data

print(data[:3])
