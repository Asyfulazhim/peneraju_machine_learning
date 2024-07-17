import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize

# Load the movie review dataset
df = pd.read_csv('input.csv')

# Shuffle the data
df = df.sample(frac=1, random_state=10)

# Set featureset size as 600
vectorizer = TfidfVectorizer(max_features=600)

# Split the data into training and testing data
X = df['review']
y = df['sentiment']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

# Convert text data into feature vectors
X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)

# Train the LinearSVC classifier
LinearSVC_classifier = LinearSVC()
LinearSVC_classifier.fit(X_train_vectors, y_train)

# Make predictions on the testing data
y_pred_LinearSVC = LinearSVC_classifier.predict(X_test_vectors)

# Calculate the accuracy of the LinearSVC classifier
accuracy_LinearSVC = accuracy_score(y_test, y_pred_LinearSVC)

# Train the NaiveBayesClassifier
nltk_data = [(dict([(word, True) for word in word_tokenize(review)]), sentiment) for review, sentiment in zip(X_train, y_train)]
naive_bayes_classifier = NaiveBayesClassifier.train(nltk_data)

# Make predictions on the testing data
y_pred_nb = [naive_bayes_classifier.classify(dict([(word, True) for word in word_tokenize(review)])) for review in X_test]

# Calculate the accuracy of the NaiveBayesClassifier
accuracy_nb = accuracy_score(y_test, y_pred_nb)

# Print the accuracy of both classifiers
print("Naive Bayes Accuracy {:.2f}% using nltk".format(accuracy_nb * 100))
print("LinearSVC_classifier Accuracy {:.2f}% using scikit-learn".format(accuracy_LinearSVC * 100))