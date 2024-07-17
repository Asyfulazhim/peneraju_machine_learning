from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

iris = datasets.load_iris()
X = iris.data
y = iris.target
test_data = float(input("Enter the test size (as a decimal, e.g., 0.2 for 20%): \n"))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_data, random_state=42)
sv = SVC(kernel='linear')
sv.fit(X_train, y_train)
y_predict = sv.predict(X_test)

accuracy = accuracy_score(y_test, y_predict) * 100
correct = (accuracy/100)* len(y_predict)
wrong = len(y_predict) - correct

print(f"Accuracy: {accuracy:.2f}%")
print(f"Correct Predictions: {int(correct)}")
print(f"Wrong Predictions: {int(wrong)}")