# svm_algorithm.py

"""
Support Vector Machine (SVM) Algorithm
=====================================

Introduction
------------

SVM is a supervised machine learning algorithm used for classification and regression tasks.
It tries to find the best boundary (hyperplane) that separates different classes in the data.
The main goal of SVM is to maximize the margin between the two classes.

Key Concepts
-------------

1. **Hyperplane**: A decision boundary separating different classes in feature space.
2. **Support Vectors**: The closest data points to the hyperplane, crucial for determining the hyperplane and margin.
3. **Margin**: The distance between the hyperplane and the support vectors.
4. **Kernel**: A function that maps data to a higher-dimensional space, enabling SVM to handle non-linearly separable data.
5. **C**: A regularization term balancing margin maximization and misclassification penalties.

Types of Support Vector Machine
--------------------------------

1. **Linear SVM**: Uses a linear decision boundary to separate classes.
2. **Non-Linear SVM**: Uses kernel functions to map data to a higher-dimensional space, handling non-linearly separable data.

How SVM Works
-------------

1. **Data Preprocessing**: Scale and normalize the data.
2. **Kernel Selection**: Choose a kernel function (e.g., linear, polynomial, RBF).
3. **Model Training**: Train the SVM model using the selected kernel.
4. **Model Evaluation**: Evaluate the model's performance using metrics (e.g., accuracy, precision, recall).

Example Use Cases
-----------------

1. **Image Classification**: SVM is used in image classification tasks, such as recognizing handwritten digits.
2. **Text Classification**: SVM is used in text classification tasks, such as spam vs. non-spam emails.
3. **Bioinformatics**: SVM is used in bioinformatics to classify protein structures and predict gene expression.

Code Implementation
-------------------
"""

# Import necessary libraries
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

def load_dataset():
    """
    Load breast cancer dataset
    """
    cancer = load_breast_cancer()
    X = cancer.data[:, :2]
    y = cancer.target
    return X, y, cancer

def split_data(X, y):
    """
    Split data into training and testing sets
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_svm(X_train, y_train):
    """
    Train SVM model
    """
    svm = SVC(kernel="linear", C=1)
    svm.fit(X_train, y_train)
    return svm

def evaluate_svm(svm, X_test, y_test):
    """
    Evaluate SVM model
    """
    y_pred = svm.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    return accuracy, report

def visualize_svm(svm, X, y, cancer):
    """
    Visualize SVM decision boundary
    """
    DecisionBoundaryDisplay.from_estimator(
        svm,
        X,
        response_method="predict",
        alpha=0.8,
        cmap="Pastel1",
        xlabel=cancer.feature_names[0],
        ylabel=cancer.feature_names[1],
    )

    plt.scatter(X[:, 0], X[:, 1], 
                c=y, 
                s=20, edgecolors="k")
    plt.show()

if __name__ == "__main__":
    X, y, cancer = load_dataset()
    X_train, X_test, y_train, y_test = split_data(X, y)
    svm = train_svm(X_train, y_train)
    accuracy, report = evaluate_svm(svm, X_test, y_test)
    print("Accuracy:", accuracy)
    print("Classification Report:\n", report)
    visualize_svm(svm, X, y, cancer)