from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# User input for dataset characteristics
num_samples = int(input("Enter the number of samples for the dataset:\n"))
num_features = int(input("Enter the number of features for each sample:\n"))
test_size = float(input("Enter the test size (as a fraction, e.g., 0.2 for 20%):\n"))
random_state = int(input("Enter the random state for dataset generation:\n"))
n_estimators = int(input("Enter the number of estimators for RandomForestClassifier:\n"))

# Generate synthetic data based on user input
X, y = make_classification(n_samples=num_samples, n_features=num_features, random_state=random_state)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

# Create a RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
rfc.fit(X_train, y_train)

# Make predictions and evaluate
y_pred = rfc.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Random Forest Classifier Accuracy: {accuracy:.2f}")