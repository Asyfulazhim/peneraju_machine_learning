import pandas as pd

data = pd.read_csv('iris_with_header.csv')

df = pd.DataFrame(data)

print(df[['sepal_length', 'sepal_width']])

#print(df.loc[:9][])