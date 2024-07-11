import pandas as pd

data = pd.read_csv('iris_with_header.csv')

df = pd.DataFrame(data)
print("DataFrame")
print(df)

print("Shape")
print(data.shape)

print("Data Types")
print(data.dtypes)  

# Display the number of columns under each data type
print("Column Count under each dtype")
print(data.dtypes.value_counts())

data_without_species = data.drop(columns=['species_type'])

print("Summary statistics ")
print(data_without_species.describe(include='all'))