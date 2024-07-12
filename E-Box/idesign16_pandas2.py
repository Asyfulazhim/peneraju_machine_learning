import pandas as pd

columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species_type']

data = pd.read_csv('iris.csv', names=columns, skiprows=1)
#print(data.head())
#print(data)
df = pd.DataFrame(data, columns=columns)
print(df)
