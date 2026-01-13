# ensemble_learning.py

"""
Ensemble learning is a machine learning technique that combines multiple models to improve prediction accuracy and robustness.
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

    # Types of Ensemble Learning
    print("# Types of Ensemble Learning:")
    print("1. Bagging (Bootstrap Aggregation): Trains multiple models on different subsets of the data and combines their predictions. Example: Random Forest.")
    print("2. Boosting: Trains models sequentially, with each model focusing on the mistakes of the previous one. Examples: AdaBoost, Gradient Boosting, XGBoost.")
    print("3. Stacking: Combines predictions from multiple models using a meta-model.")

    # Bagging (Bootstrap Aggregation)
    print("\n# Bagging (Bootstrap Aggregation)")
    bagging_clf = BaggingClassifier(base_estimator=DecisionTreeClassifier(), n_estimators=10, random_state=42)
    bagging_clf.fit(X_train, y_train)
    print("Bagging Accuracy:", bagging_clf.score(X_test, y_test))

    # Boosting
    print("\n# Boosting")
    adaboost_clf = AdaBoostClassifier(n_estimators=10, random_state=42)
    adaboost_clf.fit(X_train, y_train)
    print("AdaBoost Accuracy:", adaboost_clf.score(X_test, y_test))

    # Stacking
    print("\n# Stacking")
    estimators = [
        ('dt', DecisionTreeClassifier()),
        ('svm', SVC(probability=True))
    ]
    stacking_clf = StackingClassifier(estimators=estimators, final_estimator=LogisticRegression())
    stacking_clf.fit(X_train, y_train)
    print("Stacking Accuracy:", stacking_clf.score(X_test, y_test))

    # Benefits of Ensemble Learning
    print("\n# Benefits of Ensemble Learning:")
    print("* Improved Accuracy: Reduces errors and improves prediction precision.")
    print("* Reduced Overfitting: Combines models to generalize better to unseen data.")
    print("* Robustness: Mitigates the impact of noisy or incorrect data points.")
    print("* Flexibility: Works with diverse models, including decision trees, neural networks, and support vector machines.")

    # Examples
    print("\n# Examples:")
    print("* Finance: Fraud detection, credit scoring, and risk management.")
    print("* Healthcare: Disease diagnosis, medical image analysis.")
    print("* E-commerce: Product recommendations, customer behavior analysis.")

if __name__ == "__main__":
    main()