# decision_tree_classifier.py

"""
Implementing Decision Tree Classifiers with Scikit-Learn
"""

# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

def load_dataset():
    """
    Load the Iris dataset
    """
    data = load_iris()
    X = data.data
    y = data.target
    return X, y

def split_dataset(X, y):
    """
    Split the dataset into training and testing sets
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=99)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """
    Train a Decision Tree Classifier
    """
    clf = DecisionTreeClassifier(random_state=1)
    clf.fit(X_train, y_train)
    return clf

def evaluate_model(clf, X_test, y_test):
    """
    Evaluate the model's performance
    """
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy}')

def hyperparameter_tuning(X_train, y_train):
    """
    Perform hyperparameter tuning using GridSearchCV
    """
    param_grid = {
        'max_depth': range(1, 10, 1),
        'min_samples_leaf': range(1, 20, 2),
        'min_samples_split': range(2, 20, 2),
        'criterion': ["entropy", "gini"]
    }

    tree = DecisionTreeClassifier(random_state=1)
    grid_search = GridSearchCV(estimator=tree, param_grid=param_grid, cv=5, verbose=True)
    grid_search.fit(X_train, y_train)
    print("Best accuracy", grid_search.best_score_)
    print(grid_search.best_estimator_)
    return grid_search.best_estimator_

def visualize_tree(tree_clf, iris):
    """
    Visualize the Decision Tree
    """
    plt.figure(figsize=(18, 15))
    plot_tree(tree_clf, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
    plt.show()

if __name__ == "__main__":
    # Load the dataset
    X, y = load_dataset()
    iris = load_iris()

    # Split the dataset
    X_train, X_test, y_train, y_test = split_dataset(X, y)

    # Train the model
    clf = train_model(X_train, y_train)

    # Evaluate the model
    evaluate_model(clf, X_test, y_test)

    # Perform hyperparameter tuning
    best_clf = hyperparameter_tuning(X_train, y_train)

    # Visualize the Decision Tree
    visualize_tree(best_clf, iris)