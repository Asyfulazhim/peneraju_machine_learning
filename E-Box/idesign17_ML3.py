import pandas as pd
import numpy as np

# Load the dataset from a CSV file
data = pd.read_csv('dataset.csv')
#print(data)
# Calculate the total number of records
total_records = len(data)

# Calculate the number of records containing 'golf'
golf_count = len(data[data['recreation'] == 'golf'])

# Calculate the unconditional probability of 'golf'
unconditional_golf = golf_count / total_records
#print(unconditional_golf)

# Calculate the conditional probability of 'single' given 'medRisk'
medRisk_count = len(data[data['credit_worthiness'] == 'medRisk'])
single_and_medRisk_count = len(data[(data['credit_worthiness'] == 'medRisk') & (data['status'] == 'single')])
conditional_probability_single_given_medRisk = single_and_medRisk_count / medRisk_count

print(f"Unconditional probability of golf: = {unconditional_golf:.2f}")
print(f"Conditional probability of single given medRisk: = {conditional_probability_single_given_medRisk:.2f}")

#Unconditional probability of golf: = 0.40
#Conditional probability of single given medRisk: = 0.67