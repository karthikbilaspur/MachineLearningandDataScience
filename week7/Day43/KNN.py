# KNN (K-Nearest Neighbors) Algorithm 😊

# Import necessary libraries
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris, load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# What is KNN?
# KNN is a supervised learning algorithm used for classification and regression tasks.
# It's a simple, non-parametric, and lazy learning algorithm.

# What is K in KNN?
# K is the number of nearest neighbors to consider when making a prediction.

# Methods:
# * Classification: KNN classifies a new instance by a majority vote of its K nearest neighbors.
# * Regression: KNN predicts the target value by taking the average of the target values of its K nearest neighbors.

# Metrics used in KNN:
# * Euclidean Distance: √(∑(xi - yi)^2)
# * Manhattan Distance: ∑|xi - yi|
# * Minkowski Distance: (∑|xi - yi|^p)^(1/p)
# * Cosine Similarity: (A · B) / (|A| |B|)

def knn_example():
    # Load iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a KNN classifier
    knn = KNeighborsClassifier(n_neighbors=5)

    # Train the model
    knn.fit(X_train, y_train)

    # Make predictions
    y_pred = knn.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

def knn_digits_example():
    # Load digits dataset
    digits = load_digits()
    X = digits.data
    y = digits.target

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a KNN classifier
    knn = KNeighborsClassifier(n_neighbors=5)

    # Train the model
    knn.fit(X_train, y_train)

    # Make predictions
    y_pred = knn.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

# Applications:
# * Image Classification: Handwritten digit recognition, facial recognition
# * Recommendation Systems: Product recommendation, movie recommendation
# * Text Classification: Sentiment analysis, spam detection
# * Medical Diagnosis: Disease diagnosis, patient classification

# Advantages:
# * Simple to implement: Easy to understand and implement
# * No training time: No explicit training phase
# * Robust to noise: Can handle noisy data

# Disadvantages:
# * High computational cost: High prediction time complexity
# * Sensitive to K: Choice of K affects performance
# * Sensitive to irrelevant features: Can be affected by irrelevant features

if __name__ == "__main__":
    print("KNN Example:")
    knn_example()
    print("\nKNN Digits Example:")
    knn_digits_example()