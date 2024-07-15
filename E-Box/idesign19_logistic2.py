import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold, LeaveOneOut
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
import seaborn as sns
from sklearn import __version__ as sklearn_version

# Load the dataset
data = pd.read_csv('heart_disease.csv')
#print(data)

# Extracting features and target
X = data.drop('target', axis=1)
y = data['target']

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Implement Logistic Regression
model = LogisticRegression()

# Validation approaches
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

#Validation set approach
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
#print(f'Validation set approach - Accuracy: {accuracy:.2f}')

# K-fold cross validation(use cv=5, scoring='accuracy')
kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X_scaled, y, cv=kfold, scoring='accuracy')
#print(f'K-fold cross validation - Accuracy: {np.mean(scores):.2f}')

#Stratified K-fold cross validation(n_splits=5, shuffle=True, random_state=42)
skfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X_scaled, y, cv=skfold, scoring='accuracy')
#print(f'Stratified K-fold cross validation - Accuracy: {np.mean(scores):.2f}')

#LOO strategy
loo = LeaveOneOut()
scores = cross_val_score(model, X_scaled, y, cv=loo, scoring='accuracy')
#print(f'LOO strategy - Accuracy: {np.mean(scores):.2f}')

# c. Plot Confusion Matrix
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.savefig("ConfusionMatrix.png")

# d. Report performance metrics with two decimal points
precision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average='weighted')

print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1 Score: {f1:.2f}')
