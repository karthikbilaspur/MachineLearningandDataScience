# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

def main():
    # What is Naive Bayes?
    # Naive Bayes is a family of probabilistic machine learning models based on Bayes' theorem.
    # It's a simple, yet powerful algorithm for classification tasks.

    # Bayes' Theorem:
    # P(y|X) = P(X|y) * P(y) / P(X)
    # where:
    # - P(y|X) is the posterior probability of class y given features X
    # - P(X|y) is the likelihood of features X given class y
    # - P(y) is the prior probability of class y
    # - P(X) is the marginal probability of features X

    # Types of Naive Bayes Classifiers:
    # 1. Gaussian Naive Bayes (GNB): assumes continuous features follow a Gaussian distribution.
    # 2. Multinomial Naive Bayes (MNB): assumes features are multinomially distributed.
    # 3. Bernoulli Naive Bayes (BNB): assumes features are binary (0/1).

    # Applications:
    # 1. Text classification (spam detection, sentiment analysis)
    # 2. Image classification
    # 3. Recommendation systems
    # 4. Medical diagnosis

    # Advantages:
    # 1. Simple to implement
    # 2. Fast training time
    # 3. Handles high-dimensional data
    # 4. Robust to irrelevant features

    # Disadvantages:
    # 1. Assumes independence between features (naive assumption)
    # 2. Can be sensitive to outliers
    # 3. Not suitable for regression tasks

    # Example: Iris dataset classification using Gaussian Naive Bayes
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    y_pred = gnb.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Gaussian Naive Bayes assumptions:
    # 1. Features are continuous and follow a Gaussian distribution
    # 2. Features are independent (naive assumption)

    # Gaussian Naive Bayes formula:
    # P(x|y) = (1 / sqrt(2 * pi * sigma^2)) * exp(-((x - mu)^2) / (2 * sigma^2))
    # where:
    # - x is the feature value
    # - mu is the mean of the feature
    # - sigma is the standard deviation of the feature

if __name__ == "__main__":
    main()