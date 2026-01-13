# Logistic Regression
# 🤔 A popular algorithm for classification problems! Let's dive in 🚀.

# What is Logistic Regression?
# - A linear model for binary classification (0/1, yes/no, etc.)
# - Predicts probabilities of belonging to a class
# - Simple, interpretable, and widely used 😊

# Key concepts:
#   - Sigmoid function (maps linear output to probabilities)
#   - Log loss (cost function to minimize)
#   - Maximum likelihood estimation (MLE)

# Let's see it in action 😎!

# Import necessary libraries
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Load iris dataset (binary classification)
iris = load_iris()
X = iris.data[:100]  # first 100 samples (2 classes)
y = iris.target[:100]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Get coefficients (weights)
print("Coefficients:", model.coef_)

# Get intercept (bias)
print("Intercept:", model.intercept_)

# Predict probabilities
y_pred_proba = model.predict_proba(X_test)
print("Predicted probabilities:", y_pred_proba)

# Plot decision boundary (2D)
if X.shape[1] == 2:
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Decision Boundary')
    plt.show()

# Regularization (L1, L2, or Elastic Net)
# - Helps prevent overfitting
model_l1 = LogisticRegression(penalty='l1', solver='liblinear', C=0.1)
model_l1.fit(X_train, y_train)

# Hyperparameter tuning using GridSearchCV
from sklearn.model_selection import GridSearchCV
param_grid = {'C': [0.1, 1, 10], 'penalty': ['l1', 'l2']}
grid_search = GridSearchCV(LogisticRegression(max_iter=1000), param_grid, cv=5)
grid_search.fit(X_train, y_train)
print("Best Parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)

# Want to explore more, like:
# - Multi-class logistic regression?
# - Real-world examples?
# - Other classification algorithms?
