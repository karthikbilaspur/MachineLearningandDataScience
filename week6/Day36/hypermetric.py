
# hyperparameter_tuning.py

"""
Hyperparameter Tuning
=============================================

Hyperparameter tuning is the process of selecting the optimal values for a machine learning model's hyperparameters.
"""

# Import necessary libraries
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from scipy.stats import randint
import numpy as np

# Generating sample data
X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_classes=2, random_state=42)

# GridSearchCV
# ------------

# Define hyperparameter space
c_space = np.logspace(-5, 8, 15)
param_grid = {'C': c_space}

# Initialize model
logreg = LogisticRegression()

# Perform grid search
logreg_cv = GridSearchCV(logreg, param_grid, cv=5)
logreg_cv.fit(X, y)

print("Tuned Logistic Regression Parameters (GridSearchCV): {}".format(logreg_cv.best_params_))
print("Best score is {}".format(logreg_cv.best_score_))

# RandomizedSearchCV
# ------------------

# Define hyperparameter space
param_dist = {
    "max_depth": [3, None],
    "max_features": randint(1, 9),
    "min_samples_leaf": randint(1, 9),
    "criterion": ["gini", "entropy"]
}

# Initialize model
tree = DecisionTreeClassifier()

# Perform random search
tree_cv = RandomizedSearchCV(tree, param_dist, cv=5)
tree_cv.fit(X, y)

print("Tuned Decision Tree Parameters (RandomizedSearchCV): {}".format(tree_cv.best_params_))
print("Best score is {}".format(tree_cv.best_score_))

# Bayesian Optimization
# ---------------------

# Note: Bayesian optimization is typically implemented using libraries like scikit-optimize or hyperopt.
# For simplicity, we will not implement Bayesian optimization here.

# Advantages of Hyperparameter Tuning
# ------------------------------------

# 1. Improved Model Performance
# 2. Reduced Overfitting and Underfitting
# 3. Enhanced Model Generalizability
# 4. Optimized Resource Utilization
# 5. Improved Model Interpretability

# Challenges
# ----------

# 1. Dealing with High-Dimensional Hyperparameter Spaces
# 2. Incorporating Domain Knowledge
# 3. Developing Adaptive Hyperparameter Tuning Methods