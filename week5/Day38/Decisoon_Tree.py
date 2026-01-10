# decision_tree.py

"""
What is a Decision Tree?
A Decision Tree is a type of supervised learning algorithm used for both classification and regression tasks.
It's a tree-like model that recursively partitions the data into smaller subsets based on the most informative features.

Types of Decision Trees
1. Classification Trees: Used for categorical target variables (e.g., spam vs. not spam emails)
2. Regression Trees: Used for continuous target variables (e.g., predicting house prices)

Applications of Decision Trees
1. Classification:
    - Spam filtering
    - Medical diagnosis (e.g., disease diagnosis)
    - Credit risk assessment
2. Regression:
    - Predicting continuous values (e.g., house prices, stock prices)
    - Forecasting (e.g., demand forecasting)
3. Feature Selection:
    - Identifying important features in a dataset

Uses of Decision Trees
1. Handling Missing Values: Decision Trees can handle missing values effectively.
2. Non-Linear Relationships: Decision Trees can capture non-linear relationships between features.
3. Interpretability: Decision Trees provide interpretable results, making them useful for business decision-making.

Examples
1. Medical Diagnosis: A decision tree can be used to diagnose a disease based on symptoms and medical history.
2. Credit Risk Assessment: A decision tree can be used to predict the likelihood of a customer defaulting on a loan.
3. Customer Segmentation: A decision tree can be used to segment customers based on their buying behavior.
"""

# Import necessary libraries
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.datasets import load_iris, load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error

def classification_example():
    """
    Classification Example using Decision Tree Classifier
    """
    # Load iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a decision tree classifier
    clf = DecisionTreeClassifier(random_state=42)

    # Train the model
    clf.fit(X_train, y_train)

    # Make predictions
    y_pred = clf.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Classification Accuracy:", accuracy)

def regression_example():
    """
    Regression Example using Decision Tree Regressor
    """
    # Load diabetes dataset
    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a decision tree regressor
    reg = DecisionTreeRegressor(random_state=42)

    # Train the model
    reg.fit(X_train, y_train)

    # Make predictions
    y_pred = reg.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    print("Regression Mean Squared Error:", mse)

if __name__ == "__main__":
    # Run examples
    classification_example()
    regression_example()