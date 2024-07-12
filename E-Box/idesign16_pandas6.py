import pandas as pd

colums = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species_type']
data = pd.read_csv('iris_with_header.csv')
data = pd.DataFrame(data)

print("Original  DataFrame")
print(data)


data_sorted = data.sort_values(by='sepal_length')
print("Sorted DataFrame")
print(data_sorted)
