# Prob 1
import warnings
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Suppress warnings
warnings.filterwarnings("ignore")

# Generate synthetic data with fixed random_state
X, y = make_classification(n_samples=100, n_features=5, random_state=0)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Prompt the user to input the desired voting strategy
voting_strategy = input("Enter voting strategy (hard/soft):\n")

# Create base classifiers
classifier1 = LogisticRegression(random_state=42)
classifier2 = DecisionTreeClassifier(random_state=42)

# Build a Voting Classifier using the specified strategy and a fixed random state
voting_clf = VotingClassifier(estimators=[('lr', classifier1), ('dt', classifier2)], voting=voting_strategy)

# Train the model on the training data
voting_clf.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = voting_clf.predict(X_test)

# Evaluate the accuracy of the Voting Classifier
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy result
print("Voting Classifier Accuracy:", accuracy)

# Prob 2
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

# Step 1: Load the Iris dataset
data = pd.read_csv('IRIS.csv')
#print(data)

# Step 2: Identify Features and Target
X = data.drop('Species', axis = 1)
y = data['Species']

# Step 3: Split the dataset into training and testing sets(test_size=0.3, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Create and train a Decision Tree classifier
dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)

# Step 5: Make predictions on the testing set
y_pred = dtc.predict(X_test)

# Step 6: Evaluate classifier's performance
accuracy = accuracy_score(y_test, y_pred)
#precision = precision_score(y_test, y_pred, average='weighted')
#recall = recall_score(y_test, y_pred, average='weighted')
#f1 = f1_score(y_test, y_pred, average='weighted')

print(f"Accuracy: {accuracy:.2f}")
#print("Precision:", precision)
#print("Recall:", recall)
#print("F1 Score:", f1)

feature1 = float(input("Enter value for feature 1:\n"))
feature2 = float(input("Enter value for feature 2:\n"))
feature3 = float(input("Enter value for feature 3:\n"))
feature4 = float(input("Enter value for feature 4:\n"))

new_data = [[feature1, feature2, feature3, feature4]]
new_prediction = dtc.predict(new_data)

print("Prediction for input data:", new_prediction[0])
