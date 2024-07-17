
#Step 1 : Import the required libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
import warnings
warnings.simplefilter('ignore')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

#Step 2 : Load the dataset
data = pd.read_csv('fruits.csv')
#print(data)

#Step 3 : Split dataset in features and target variable
X = data[['Weight', 'Size']]
y = data['Class']


#Step 4 : Encode the classes 'apple' and 'orange' into 0 and 1
le = LabelEncoder()
y_encode = le.fit_transform(y)
#print(y_encode)

#Step 5 : Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y_encode, test_size=0.2,shuffle=False, random_state=0)

#Step 6: Build a model (Use SVM Classifier with the following set of tuned parameters)
#'kernel': ['rbf','linear'], 'gamma': [1e-3, 1e-4], 'C': [1, 10, 100, 1000]
#3 Substeps - Create the model, Train the model, Predict response for test dataset
param_grid = {
    'kernel': ['rbf', 'linear'],
    'gamma': [1e-3, 1e-4],
    'C': [1, 10, 100, 1000]
}

sv = SVC()
grid_search = GridSearchCV(sv, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_
best_params = grid_search.best_params_

y_predict = best_model.predict(X_test)

#Step 7 : Evaluate the model 
#Compute Accuracy, Precision, Recall, F1-Score, Support and Confusion Matrix. Use average="Macro"
#Round of Accuracy, Precision, Recall and F1-Score to 2 decimal precision using round function
accuracy = accuracy_score(y_test, y_predict)
precision, recall, f1, support = precision_recall_fscore_support(y_test, y_predict, average='macro')
conf_mat = confusion_matrix(y_test, y_predict)

print("Accuracy : ", round(accuracy, 2))
print("Precision : ", round(precision, 2))
print("Recall : ", round(recall, 2))
print("F1-Score : ", round(f1, 2))
print("Support : ", support)
print("Confusion Matrix\n", conf_mat)


#Step 8 : Test the Model with new data from the user
def test_model(weight, size):
    new_data = np.array([[weight, size]])
    prediction = best_model.predict(new_data)
    #result = le.inverse_transform(prediction)[0]
    print(prediction)

weight, size =[float(s) for s in  input("Enter input data").split(",")]
test_model(weight, size)