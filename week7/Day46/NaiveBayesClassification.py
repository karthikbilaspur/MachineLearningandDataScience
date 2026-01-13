import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
newsgroups = fetch_20newsgroups(subset='all', categories=['sci.space', 'rec.sport.baseball'])

# Split data into training and testing sets
train_data, test_data, train_labels, test_labels = train_test_split(newsgroups.data, newsgroups.target, test_size=0.2, random_state=42)

# Vectorize text data using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X_train = vectorizer.fit_transform(train_data)
X_test = vectorizer.transform(test_data)

# Train a Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train, train_labels)

# Make predictions
predictions = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(test_labels, predictions)
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(test_labels, predictions))
print("Confusion Matrix:")
print(confusion_matrix(test_labels, predictions))