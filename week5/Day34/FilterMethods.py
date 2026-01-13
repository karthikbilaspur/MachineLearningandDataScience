# Feature Selection Techniques in Machine Learning
# 😊 They're like the secret ingredients that make your model recipes taste better 🤩.

# Here's a rundown of popular techniques:
# Filter Methods:
#   - Correlation Coefficient (e.g., Pearson's r)
#   - Mutual Information
#   - Variance Threshold
# Wrapper Methods:
#   - Recursive Feature Elimination (RFE)
#   - Forward Selection
#   - Backward Elimination
# Embedded Methods:
#   - Lasso Regression (L1 regularization)
#   - Ridge Regression (L2 regularization)
#   - Decision Trees (e.g., Random Forest, XGBoost)

# These techniques help you pick the most relevant features, reduce overfitting, and boost model performance 🚀.

# Let's level up with Python examples 😎!

# Filter Methods
# Correlation Coefficient (Pearson's r)
import pandas as pd
from scipy.stats import pearsonr

# Sample data
data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 3, 5, 7, 11], 'target': [3, 5, 7, 11, 13]})

# Calculate correlation
corr_coef, _ = pearsonr(data['A'], data['target'])
print(f"Correlation Coefficient: {corr_coef}")

# Mutual Information
from sklearn.feature_selection import mutual_info_classif
from sklearn.datasets import load_iris

# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Calculate mutual information
mi = mutual_info_classif(X, y)
print(mi)

# Variance Threshold
from sklearn.feature_selection import VarianceThreshold

# Sample data
X = [[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]]

# Apply variance threshold
selector = VarianceThreshold(threshold=0.5)
X_new = selector.fit_transform(X)
print(X_new)

# Wrapper Methods
# Recursive Feature Elimination (RFE)
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Apply RFE
estimator = LogisticRegression()
selector = RFE(estimator, n_features_to_select=2)
X_new = selector.fit_transform(X, y)
print(X_new.shape)

# Forward Selection
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Apply forward selection
estimator = KNeighborsClassifier(n_neighbors=3)
sfs = SequentialFeatureSelector(estimator, n_features_to_select=2, direction='forward')
X_new = sfs.fit_transform(X, y)
print(X_new.shape)

# Embedded Methods
# Lasso Regression (L1 regularization)
from sklearn.linear_model import Lasso
import numpy as np

# Sample data
X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([2, 4, 5])

# Apply Lasso regression
lasso = Lasso(alpha=0.1)
lasso.fit(X, y)
print(lasso.coef_)

# Decision Trees (Random Forest)
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Apply Random Forest
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X, y)
print(rf.feature_importances_)