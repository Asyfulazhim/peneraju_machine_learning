import pandas as pd
from sklearn.cluster import KMeans
import warnings
warnings.simplefilter("ignore")
# Read the data from the CSV file
data = pd.read_csv('dataset.csv')
#print(data)

# Select the features (VAR1 and VAR2)
features = data[['VAR1', 'VAR2']]

# Perform k-means clustering with 3 centroids
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(features)

# Define the new case to predict
new1 = float(input("Enter VAR1:\n"))
new2 = float(input("Enter VAR2:\n"))
new_case = [new1, new2]

# Predict the cluster for the new case
predicted_cluster = kmeans.predict([new_case])[0]

# Print the predicted cluster
print("Predicted Cluster for New Case: ", predicted_cluster)
