# decision_tree_algorithms.py

"""
Decision Tree Algorithms
"""

# Import necessary libraries
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris, load_diabetes
from sklearn.metrics import accuracy_score, mean_squared_error

def load_datasets():
    """
    Load datasets
    """
    iris = load_iris()
    diabetes = load_diabetes()
    return iris, diabetes

def split_data(iris, diabetes):
    """
    Split data into training and testing sets
    """
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
    X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(diabetes.data, diabetes.target, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test, X_train_reg, X_test_reg, y_train_reg, y_test_reg

def decision_tree_algorithms(X_train, X_test, y_train, y_test, X_train_reg, X_test_reg, y_train_reg, y_test_reg):
    """
    Decision Tree Algorithms
    """
    # ID3 (not implemented in Scikit-Learn)
    print("ID3 (Iterative Dichotomiser 3)")
    print("Uses information gain to split data")
    print("Classification only")
    print("Prone to overfitting, struggles with continuous data")
    print()

    # C4.5
    print("C4.5")
    print("Uses gain ratio to split data")
    print("Handles discrete and continuous data")
    print("Struggles with noisy data")
    clf_c4_5 = DecisionTreeClassifier(criterion='entropy', random_state=42)
    clf_c4_5.fit(X_train, y_train)
    y_pred_c4_5 = clf_c4_5.predict(X_test)
    print("C4.5 Accuracy:", accuracy_score(y_test, y_pred_c4_5))
    print()

    # CART
    print("CART (Classification and Regression Trees)")
    print("Uses Gini impurity for classification, MSE for regression")
    print("Handles classification and regression")
    print("Uses pruning to prevent overfitting")
    clf_cart = DecisionTreeClassifier(criterion='gini', random_state=42)
    clf_cart.fit(X_train, y_train)
    y_pred_cart = clf_cart.predict(X_test)
    print("CART Accuracy:", accuracy_score(y_test, y_pred_cart))
    reg_cart = DecisionTreeRegressor(criterion='mse', random_state=42)
    reg_cart.fit(X_train_reg, y_train_reg)
    y_pred_reg_cart = reg_cart.predict(X_test_reg)
    print("CART MSE:", mean_squared_error(y_test_reg, y_pred_reg_cart))
    print()

    # CHAID (not implemented in Scikit-Learn)
    print("CHAID (Chi-Square Automatic Interaction Detection)")
    print("Uses chi-square tests for splitting")
    print("Effective for large categorical datasets")
    print("Not suitable for continuous data")
    print()

    # MARS (not implemented in Scikit-Learn)
    print("MARS (Multivariate Adaptive Regression Splines)")
    print("Uses piecewise linear functions to model non-linear relationships")
    print("Handles regression tasks")
    print("Computationally expensive")
    print()

    # Conditional Inference Trees (not implemented in Scikit-Learn)
    print("Conditional Inference Trees")
    print("Uses statistical hypothesis testing for unbiased splits")
    print("Handles various data types")
    print("Slower than other algorithms")

if __name__ == "__main__":
    iris, diabetes = load_datasets()
    X_train, X_test, y_train, y_test, X_train_reg, X_test_reg, y_train_reg, y_test_reg = split_data(iris, diabetes)
    decision_tree_algorithms(X_train, X_test, y_train, y_test, X_train_reg, X_test_reg, y_train_reg, y_test_reg)