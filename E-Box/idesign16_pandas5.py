import pandas as pd

colums = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species_type']
data = pd.read_csv('iris_with_header.csv')
data = pd.DataFrame(data)

print("Column Names")
print(data.columns)

data.rename(columns = {'species_type' : 'SpeciesType'}, inplace = True)
print("Column Names after renaming")
print(data.columns)

print("DataFrame")
print(data)