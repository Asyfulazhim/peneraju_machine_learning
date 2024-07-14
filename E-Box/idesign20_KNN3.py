#Step 1: Import the required libraries
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix


#Step 2: Load the Dataset (file name : diabetes.csv)
df = pd.read_csv('diabetes.csv' , names = ['Pregnancies', 'Glucose', 'Blood Pressure', 'Skin Thickness', 'Insulin', 'BMI', 'DiabetisPedigree', 'Age'])
print(df)
#Step 3: Split Dataset in features and target variable

#Step 4 : Split in to Training and Test Data (20% of the data for testing)

#Step 5 : Build a model (Use KNeighborsClassifier with n_neighbors=7)
#3 Substeps - Create the model, Train the model, Predict response for test dataset

#Step 6 : Evaluate the model 
#Compute Accuracy, Precision, Recall, F1-Score, Support and Confusion Matrix
#Round of Accuracy, Precision, Recall and F1-Score to 2 decimal precision using round function

#Step 7 : Test the Model with new data from the user


import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix

# Step 2: Load the Dataset (file name : diabetes.csv)
df = pd.read_csv('diabetes.csv', names=['Pregnancies', 'Glucose', 'Blood Pressure', 'Skin Thickness', 'Insulin', 'BMI', 'DiabetisPedigree', 'Age', 'Outcome'])
print(df)

# Step 3: Split Dataset in features and target variable
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Step 4: Split into Training and Test Data (20% of the data for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False, random_state=0)

# Step 5: Build a model (Use KNeighborsClassifier with n_neighbors=7)
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# Step 6: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision, recall, f1, support = precision_recall_fscore_support(y_test, y_pred, average='weighted')
print("Accuracy: {:.2f}".format(round(accuracy, 2)))
print("Precision: {:.2f}".format(round(precision, 2)))
print("Recall: {:.2f}".format(round(recall, 2)))
print("F1-Score: {:.2f}".format(round(f1, 2)))
print("Support:", support)
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Step 7: Test the Model with new data from the user
new_data = [[0, 70, 48, 10, 0, 21, 0.124, 22], [7, 190, 70, 36, 243, 36, 0.28, 43]]
new_pred = knn.predict(new_data)
print("Predicted outcomes for new data:")
print(new_pred)