import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Load the dataset
df = pd.read_csv('input.csv', names=['sepal length', 'sepal width', 'petal length', 'petal width', 'species'])

# Select the first row as the test vector
test_vector = df.iloc[0][['sepal length', 'sepal width', 'petal length', 'petal width']].values.reshape(1, -1)

# Create a Nearest Neighbors model with K=3
nn = NearestNeighbors(n_neighbors=3)

# Fit the model to the dataset
nn.fit(df[['sepal length', 'sepal width', 'petal length', 'petal width']])

# Find the top 3 nearest neighbors of the test vector
distances, indices = nn.kneighbors(test_vector)

# Get the nearest neighbors
nearest_neighbors = df.iloc[indices[0]][['sepal length', 'sepal width', 'petal length', 'petal width']].values

# Print the nearest neighbors
for neighbor in nearest_neighbors:
    print('[' + ', '.join(map(str, neighbor)) + ']')