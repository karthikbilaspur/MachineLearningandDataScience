# decision_tree_regression.py

"""
Implementing Decision Tree Regression using Scikit-Learn
"""

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def create_dataset():
    """
    Create a synthetic dataset
    """
    np.random.seed(42)
    X = np.sort(5 * np.random.rand(100, 1), axis=0)
    y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])
    return X, y

def split_dataset(X, y):
    """
    Split the dataset into training and testing sets
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """
    Train a Decision Tree Regressor
    """
    regressor = DecisionTreeRegressor(max_depth=4, random_state=42)
    regressor.fit(X_train, y_train)
    return regressor

def evaluate_model(regressor, X_test, y_test):
    """
    Evaluate the model's performance
    """
    y_pred = regressor.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse:.4f}")

def visualize_data(X, y):
    """
    Visualize the dataset
    """
    plt.scatter(X, y, color='red', label='Data')
    plt.title("Synthetic Dataset")
    plt.xlabel("Feature")
    plt.ylabel("Target")
    plt.legend()
    plt.show()

def visualize_regression(regressor, X, y):
    """
    Visualize the regression line
    """
    X_grid = np.arange(min(X), max(X), 0.01)[:, np.newaxis]
    y_grid_pred = regressor.predict(X_grid)

    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color='red', label='Data')
    plt.plot(X_grid, y_grid_pred, color='blue', label='Model Prediction')
    plt.title("Decision Tree Regression")
    plt.xlabel("Feature")
    plt.ylabel("Target")
    plt.legend()
    plt.show()

def visualize_tree(regressor):
    """
    Visualize the Decision Tree structure
    """
    plt.figure(figsize=(20, 10))
    plot_tree(
        regressor,
        feature1_names=["Feature"],
        filled=True,
        rounded=True,
        fontsize=10
    )
    plt.title("Decision Tree Structure")
    plt.show()

if __name__ == "__main__":
    # Create a synthetic dataset
    X, y = create_dataset()

    # Visualize the dataset
    visualize_data(X, y)

    # Split the dataset
    X_train, X_test, y_train, y_test = split_dataset(X, y)

    # Train the model
    regressor = train_model(X_train, y_train)

    # Evaluate the model
    evaluate_model(regressor, X_test, y_test)

    # Visualize the regression line
    visualize_regression(regressor, X, y)

    # Visualize the Decision Tree structure
    visualize_tree(regressor)