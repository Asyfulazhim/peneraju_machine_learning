import pandas as pd
import numpy as np 

data = pd.read_csv('training_data.csv')
data = pd.DataFrame(data)

print("Dataset after removing duplicate rows:\n")
drop_row = data.drop_duplicates()
print(drop_row)

cols_to_drop = []
for col in drop_row.columns:
    if drop_row[col].nunique() == 1:
        cols_to_drop.append(col)

drop_unique_column = drop_row.drop(columns=cols_to_drop)
print("Dataset after removing columns with a single value:\n")
print(drop_unique_column)


