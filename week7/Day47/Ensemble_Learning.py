# ensemble_learning.py

"""
Ensemble Learning is a machine learning technique that combines multiple models to improve prediction accuracy and robustness.
Think of it like asking a group of experts for advice instead of relying on just one person - you're likely to get a more accurate answer 😊.
"""

# Import necessary libraries
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier, StackingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def main():
    # Load iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Bagging (Bootstrap Aggregating)
    print("# Bagging (Bootstrap Aggregating)")
    print("Bagging is a technique that involves creating multiple versions of a model and combining their outputs to improve overall performance.")
    bagging_clf = BaggingClassifier(base_estimator=DecisionTreeClassifier(), n_estimators=10, random_state=42)
    bagging_clf.fit(X_train, y_train)
    print("Bagging Accuracy:", bagging_clf.score(X_test, y_test))

    # Common Algorithms Using Bagging
    print("\n# Common Algorithms Using Bagging")
    print("1. Random Forest: An ensemble method based on decision trees, trained using different bootstrapped samples of the data.")
    print("2. Bagged Decision Trees: Multiple decision trees trained using bootstrapped samples of the data.")

    # Boosting
    print("\n# Boosting")
    print("Boosting is an ensemble technique where multiple models are trained sequentially, with each new model attempting to correct the errors made by the previous ones.")
    adaboost_clf = AdaBoostClassifier(n_estimators=10, random_state=42)
    adaboost_clf.fit(X_train, y_train)
    print("AdaBoost Accuracy:", adaboost_clf.score(X_test, y_test))

    # Common Algorithms Using Boosting
    print("\n# Common Algorithms Using Boosting")
    print("1. AdaBoost (Adaptive Boosting): Works by adjusting the weights of misclassified instances and combining the predictions of weak learners.")
    print("2. Gradient Boosting: A more general approach to boosting that builds models sequentially, with each new model fitting the residual errors of the previous model.")
    print("3. XGBoost (Extreme Gradient Boosting): An optimized version of gradient boosting with regularization and parallelization.")

    # Stacking
    print("\n# Stacking")
    print("Stacking combines multiple models of different types, where each model makes independent predictions and a meta-model is trained to combine these predictions.")
    estimators = [
        ('dt', DecisionTreeClassifier()),
        ('svm', SVC(probability=True))
    ]
    stacking_clf = StackingClassifier(estimators=estimators, final_estimator=LogisticRegression())
    stacking_clf.fit(X_train, y_train)
    print("Stacking Accuracy:", stacking_clf.score(X_test, y_test))

    # Common Algorithms Using Stacking
    print("\n# Common Algorithms Using Stacking")
    print("1. Generalized Stacking: Multiple different models trained on the same dataset.")
    print("2. Stacking with Cross-Validation: Base models trained using cross-validation and their predictions used to train the meta-model.")
    print("3. Multi-Layer Stacking: Multiple levels of base models, where the outputs of the first level are fed into the second level and so on.")

if __name__ == "__main__":
    main()