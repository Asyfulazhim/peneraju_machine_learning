import warnings
warnings.simplefilter("ignore")
from sklearn.ensemble import BaggingClassifier
from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load Digits dataset
digits = load_digits()

# User input: test size for splitting the dataset
test_size = float(input("Enter test size for dataset split (e.g., 0.2 for 20% test data):\n"))

# Split dataset
X = digits.data
y = digits.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

# User input: number of estimators and maximum features
n_estimators = int(input("Enter the number of estimators (e.g., 50):\n"))
max_features = float(input("Enter the maximum features (e.g., 0.8 for 80%):\n"))

# Create a Bagging Classifier with SVM (Random Patches)
bagging_classifier = BaggingClassifier(base_estimator=SVC(probability=True), n_estimators=n_estimators, max_samples=1.0, max_features=max_features, random_state=42)

# Train and evaluate the Bagging Classifier
bagging_classifier.fit(X_train, y_train)
y_pred = bagging_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred) * 100

print(f"Bagging Classifier (Random Patches) Accuracy: {accuracy:.2f}%")