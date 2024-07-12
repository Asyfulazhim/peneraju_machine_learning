# Prob1
import pandas as pd

df1 = pd.DataFrame([["Anitha",7.8,8.9], ["Baskar",5.6,6.9]], columns = ["student_name","sem1_cgpa", "sem2_cgpa"])
df2 = pd.DataFrame([["Anitha","CSE"], ["Baskar","IT"]], columns = ["student_name","department"])

# Fill in the code here
print("DataFrame1")
print(df1)
print("DataFrame2")
print(df2)

merged_data = pd.merge(df1, df2, on = 'student_name')
merged_data = merged_data[['student_name', 'department', 'sem1_cgpa', 'sem2_cgpa']]
print("Merged DataFrame")
print(merged_data)

#Prob2
import pandas as pd

data = pd.read_csv('iris_duplicates.csv')
df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

# By default, it removes duplicate rows based on all columns.
# To remove duplicates on specific column(s), use subset.
# df.drop_duplicates(subset=['brand'])
drop = df.drop_duplicates()
print("DataFrame after removing duplicates")
print(drop)
