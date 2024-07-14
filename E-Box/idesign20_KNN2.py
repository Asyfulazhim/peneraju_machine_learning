import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv( 'input.csv' , names=['sepal length', 'sepal width', 'petal length', 'petal width', 'species'])

le = LabelEncoder()
df['species'] = le.fit_transform(df['species'])

# Split the data into input features (X) and output variable (y)
X = df[['sepal length']]
y = df['species']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a KNN classifier with K=11
knn = KNeighborsClassifier(n_neighbors=11)

# Train the model on the training data
knn.fit(X_train, y_train)

# Get the test data from the user
test_vector = X_test

# Predict the class of the test data using the model
predicted_class = knn.predict([test_vector])[0]

# Print the predicted class
print(f"Actual Class: {y_test}")
print(f"Predicted Class: {predicted_class}")