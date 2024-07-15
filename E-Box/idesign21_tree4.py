import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

# Step 1: Load the Iris dataset
data = pd.read_csv('IRIS.csv')
#print(data)

# Features and Target
X = data[['Sepal_Length' , 'Sepal_Width', 'Petal_Length', 'Petal_Width']]
y = data['Species']

# Step 3: Split the dataset into training and testing sets(test_size=0.3, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)

# Step 5: Make predictions on the testing set
clf = DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

# Step 5: Make predictions on the testing set
predictions = clf.predict(X_test)

# Step 6: Evaluate classifier's performance
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions, average='weighted')
recall = recall_score(y_test, predictions, average='weighted')
f1 = f1_score(y_test, predictions, average='weighted')

print("Accuracy: {:.2f}".format(accuracy))
print("Precision: {:.2f}".format(precision))
print("Recall: {:.2f}   ".format(recall))
print("F1-Score: {:.2f}".format(f1))

