# Import necessary libraries
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def gaussian_naive_bayes():
    """
    Gaussian Naive Bayes (GNB) is a type of Naive Bayes classifier that assumes the features follow a Gaussian distribution.
    """
    # Load iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a Gaussian Naive Bayes classifier
    gnb = GaussianNB()

    # Train the model
    gnb.fit(X_train, y_train)

    # Make predictions
    y_pred = gnb.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Print mean and variance for each feature in each class
    for i in range(gnb.classes_.shape[0]):
        print("Class", i)
        print("Mean:", gnb.theta_[i])
        print("Variance:", gnb.sigma_[i])

    # How Gaussian Naive Bayes Works
    print("\nHow Gaussian Naive Bayes Works:")
    print("-----------------------------------")
    print("1. Assumption: The features follow a Gaussian distribution.")
    print("2. Calculate Mean and Variance: Calculate the mean and variance for each feature in each class.")
    print("3. Calculate Likelihood: Calculate the likelihood of each feature given the class using the Gaussian probability density function (PDF).")
    print("   P(x|y) = (1 / sqrt(2 * pi * sigma^2)) * exp(-((x - mu)^2) / (2 * sigma^2))")
    print("4. Calculate Posterior: Calculate the posterior probability of each class given the features using Bayes' theorem.")
    print("   P(y|x) = P(x|y) * P(y) / P(x)")
    print("5. Predict: Predict the class with the highest posterior probability.")
    print("   y_pred = argmax(P(y|x))")

if __name__ == "__main__":
    gaussian_naive_bayes()