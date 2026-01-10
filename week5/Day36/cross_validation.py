
# cross_validation.py

"""
Cross Validation in Machine Learning
=============================================

Cross-validation is a technique used to check how well a machine learning model performs on unseen data while preventing overfitting.
"""

# Import necessary libraries
from sklearn.model_selection import cross_val_score, KFold
from sklearn.svm import SVC
from sklearn.datasets import load_iris
import numpy as np

# Loading the dataset
iris = load_iris()
X, y = iris.data, iris.target

# Creating SVM classifier
svm_classifier = SVC(kernel='linear')

# Defining the number of folds for cross-validation
num_folds = 5
kf = KFold(n_splits=num_folds, shuffle=True, random_state=42)

# Performing k-fold cross-validation
cross_val_results = cross_val_score(svm_classifier, X, y, cv=kf)

# Evaluation metrics
print("Cross-Validation Results (Accuracy):")
for i, result in enumerate(cross_val_results, 1):
    print(f"  Fold {i}: {result * 100:.2f}%")
    
print(f'Mean Accuracy: {cross_val_results.mean()* 100:.2f}%')

# Types of Cross-Validation
# 1. Holdout Validation
# 2. LOOCV (Leave One Out Cross Validation)
# 3. Stratified Cross-Validation
# 4. K-Fold Cross Validation

# Holdout Validation
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)
svm_classifier.fit(X_train, y_train)
print("Holdout Validation Accuracy:", svm_classifier.score(X_test, y_test))

# LOOCV (Leave One Out Cross Validation)
from sklearn.model_selection import LeaveOneOut
loo = LeaveOneOut()
cross_val_results_loo = cross_val_score(svm_classifier, X, y, cv=loo)
print("LOOCV Accuracy:", cross_val_results_loo.mean())

# Stratified Cross-Validation
from sklearn.model_selection import StratifiedKFold
skf = StratifiedKFold(n_splits=num_folds, shuffle=True, random_state=42)
cross_val_results_stratified = cross_val_score(svm_classifier, X, y, cv=skf)
print("Stratified Cross-Validation Accuracy:", cross_val_results_stratified.mean())

# K-Fold Cross Validation
kf = KFold(n_splits=num_folds, shuffle=True, random_state=42)
cross_val_results_kfold = cross_val_score(svm_classifier, X, y, cv=kf)
print("K-Fold Cross Validation Accuracy:", cross_val_results_kfold.mean())