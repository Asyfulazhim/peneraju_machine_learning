import numpy as np
import pandas as pd

data = pd.read_csv('sample_data.csv')

columns_name = data.columns.values
#print(columns_name)

array = np.array(data)
tostring  = array.astype(str)
#print(tostring)

array_with_column_names = np.vstack([columns_name, tostring])

print(array_with_column_names)



#\print(tostring)
