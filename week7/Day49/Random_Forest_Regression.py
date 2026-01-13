"""
What is Random Forest Regression?
Random Forest Regression is a type of supervised learning algorithm that uses multiple decision trees to predict continuous outcomes.
It's an ensemble learning method that combines the predictions of multiple decision trees to produce a more accurate and robust prediction.

Example:
Suppose we want to predict the price of a house based on its features such as number of bedrooms, number of bathrooms, location, etc.
We can use Random Forest Regression to train a model on a dataset of houses with their features and prices.
The model will learn to predict the price of a new house based on its features.

Advantages:
- Handles non-linear relationships: Random Forest Regression can handle non-linear relationships between features and target variable.
- Robust to outliers: Random Forest Regression is robust to outliers and noisy data.
- Handles missing values: Random Forest Regression can handle missing values in the data.
- Improves accuracy: Random Forest Regression can improve the accuracy of predictions by combining multiple decision trees.
- Fast training: Random Forest Regression is fast to train, especially when compared to other ensemble methods.

Disadvantages:
- Black box nature: Random Forest Regression is a black box model, meaning it's difficult to interpret the results.
- Overfitting: Random Forest Regression can suffer from overfitting if the number of trees is too large.
- Slow prediction: Random Forest Regression can be slow to make predictions, especially when the number of trees is large.
- Not suitable for high-dimensional data: Random Forest Regression is not suitable for high-dimensional data (i.e., data with a large number of features).
"""

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def main():
    # Generate some sample data
    np.random.seed(0)
    X = np.random.rand(100, 3)
    y = 3 * X[:, 0] + 2 * X[:, 1] + np.random.randn(100)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a Random Forest Regressor
    rf = RandomForestRegressor(n_estimators=100, random_state=42)

    # Train the model
    rf.fit(X_train, y_train)

    # Make predictions
    y_pred = rf.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'Mean Squared Error: {mse:.2f}')
    print(f'Mean Absolute Error: {mae:.2f}')
    print(f'R-squared Score: {r2:.2f}')

if __name__ == "__main__":
    main()