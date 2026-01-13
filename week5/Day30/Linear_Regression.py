# linear_regression.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

# Simple Linear Regression
def simple_linear_regression():
    # Generating Random Dataset
    np.random.seed(42)
    X = np.random.rand(50, 1) * 100  
    Y = 3.5 * X + np.random.randn(50, 1) * 20 

    # Creating and Training Linear Regression Model
    model = LinearRegression()
    model.fit(X, Y)

    # Predicting Y Values
    Y_pred = model.predict(X)

    # Visualizing the Regression Line
    plt.figure(figsize=(8,6)) 
    plt.scatter(X, Y, color='blue', label='Data Points') 
    plt.plot(X, Y_pred, color='red', linewidth=2, label='Regression Line') 
    plt.title('Linear Regression on Random Dataset')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Slope and Intercept
    print("Slope (Coefficient):", model.coef_[0][0])
    print("Intercept:", model.intercept_[0])

# Multiple Linear Regression
def multiple_linear_regression():
    # Load dataset
    dataset = fetch_california_housing()
    X = dataset.data
    y = dataset.target

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate model
    print("Coefficient of Determination (R-squared):", model.score(X_test, y_test))

# Advantages and Limitations of Linear Regression
def advantages_and_limitations():
    print("Advantages:")
    print("1. Simple and Interpretable: Linear regression is a straightforward algorithm to understand and interpret.")
    print("2. Fast Training: Linear regression is computationally efficient and can handle large datasets quickly.")
    print("3. Well-suited for Linear Relationships: Linear regression performs well when the relationship between the independent and dependent variables is linear.")
    print("4. Provides Coefficients: Linear regression provides coefficients that can be used to understand the relationship between the independent variables and the dependent variable.")

    print("\nLimitations:")
    print("1. Assumes Linearity: Linear regression assumes a linear relationship between the independent and dependent variables, which may not always be the case.")
    print("2. Sensitive to Outliers: Linear regression is sensitive to outliers, which can significantly impact the model's performance.")
    print("3. Multicollinearity: Linear regression is sensitive to multicollinearity, which occurs when there is a high correlation between independent variables.")
    print("4. Not Suitable for Complex Relationships: Linear regression is not suitable for complex relationships between variables, such as non-linear relationships or interactions between variables.")
    print("5. Overfitting and Underfitting: Linear regression is prone to overfitting and underfitting, especially when dealing with small datasets or complex models.")

    print("\nWhen to Use Linear Regression:")
    print("1. Linear Relationships: Use linear regression when the relationship between the independent and dependent variables is linear.")
    print("2. Simple Models: Use linear regression when you want a simple and interpretable model.")
    print("3. Fast Training: Use linear regression when you need a model that can be trained quickly.")

    print("\nWhen Not to Use Linear Regression:")
    print("1. Non-Linear Relationships: Avoid using linear regression when the relationship between the independent and dependent variables is non-linear.")
    print("2. Complex Models: Avoid using linear regression when you need a complex model that can handle interactions between variables.")
    print("3. Small Datasets: Avoid using linear regression when dealing with small datasets, as it may lead to overfitting or underfitting.")

if __name__ == "__main__":
    simple_linear_regression()
    multiple_linear_regression()
    advantages_and_limitations()