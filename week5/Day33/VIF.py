# multicollinearity.py

"""
Multicollinearity in Linear Regression
=====================================

Multicollinearity occurs when predictor variables are highly correlated,
making it hard to interpret the model.
"""

# Types of Multicollinearity
types_of_multicollinearity = [
    "Perfect Multicollinearity: One variable is a linear combination of others.",
    "Imperfect Multicollinearity: Variables are highly correlated but not perfectly.",
    "Structural Multicollinearity: Variables are related due to their creation or definition.",
    "Data-based Multicollinearity: Variables are related naturally in the data."
]

# Problems with Multicollinearity
problems_with_multicollinearity = [
    "Unstable coefficients",
    "Reduced interpretability",
    "Less reliable predictions",
    "Risk of overfitting"
]

# Detecting Multicollinearity
detecting_multicollinearity = [
    "Variance Inflation Factor (VIF): Measures how much variance is inflated due to correlation.",
    "Correlation Matrix: Shows correlation coefficients between variables.",
    "Pairwise Scatter Plots: Visualizes relationships between variables."
]

# What is VIF?
vif_explanation = """
Variance Inflation Factor (VIF)
-----------------------------

VIF is a measure of how much the variance of a regression coefficient is inflated
due to correlation with other predictor variables.

VIF Formula:
VIF = 1 / (1 - R^2)

where R^2 is the coefficient of determination of the regression of the predictor
variable on all other predictor variables.

Interpretation:
* VIF = 1: No correlation
* 1 < VIF < 5: Moderate correlation
* VIF >= 5: High correlation (may indicate multicollinearity)
"""

# Handling Multicollinearity
handling_multicollinearity = [
    "Remove Redundant Variables: Drop one of the correlated variables.",
    "Combine Variables: Merge correlated variables into a single feature.",
    "Regularization Techniques: Use Ridge or Lasso regression to shrink coefficients.",
    "Collect More Data: Increase dataset size to stabilize relationships.",
    "Principal Component Analysis (PCA): Transform correlated variables into uncorrelated ones."
]

# Impact on Other Models
impact_on_other_models = [
    "Decision Trees: Not significantly affected",
    "Random Forests: Can handle correlated features but may overfit",
    "Support Vector Machines (SVM): May struggle with correlated features",
    "K-Nearest Neighbors (KNN): Correlated features can mislead distance calculations",
    "Neural Networks: May struggle with correlated features, leading to inaccurate predictions"
]

# Print the information
print("Types of Multicollinearity:")
for item in types_of_multicollinearity:
    print(f"* {item}")

print("\nProblems with Multicollinearity:")
for item in problems_with_multicollinearity:
    print(f"* {item}")

print("\nDetecting Multicollinearity:")
for item in detecting_multicollinearity:
    print(f"* {item}")

print(vif_explanation)

print("Handling Multicollinearity:")
for item in handling_multicollinearity:
    print(f"* {item}")

print("Impact on Other Models:")
for item in impact_on_other_models:
    print(f"* {item}")