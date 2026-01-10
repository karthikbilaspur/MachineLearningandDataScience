# calculus_in_data_science.py

"""
Use of Calculus in Data Science
================================

Calculus is a fundamental tool in data science, used for tasks such as optimization, gradient descent, 
and integration.

Optimization
------------

Optimization is the process of finding the best solution among a set of possible solutions. In data 
science, optimization is used to train machine learning models.

Gradient Descent
----------------

Gradient descent is an optimization algorithm used to minimize the loss function of a machine learning 
model. It works by iteratively updating the model parameters in the direction of the negative gradient 
of the loss function.

Integration
------------

Integration is used in data science to compute the area under curves, volumes of solids, and other 
quantities.

Python Implementation
---------------------

Here is an example implementation of calculus in data science using Python:
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Define a function to optimize
def f(x: float) -> float:
    return x**2 + 2*x + 1

# Define the derivative of the function
def df(x: float) -> float:
    return 2*x + 2

# Define the gradient descent algorithm
def gradient_descent(f: callable, df: callable, x0: float, learning_rate: float, num_iterations: int) -> float:
    x = x0
    for i in range(num_iterations):
        x = x - learning_rate * df(x)
    return x

# Optimize the function using gradient descent
x0 = 10
learning_rate = 0.1
num_iterations = 100
x_opt = gradient_descent(f, df, x0, learning_rate, num_iterations)
print("Optimal value of x:", x_opt)

# Optimize the function using SciPy's minimize function
res = minimize(f, x0)
print("Optimal value of x (SciPy):", res.x)

# Plot the function
x = np.linspace(-10: 10, 100)
y = f(x)
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function to Optimize")
plt.show()

# Integration
from scipy.integrate import quad

# Define a function to integrate
def f(x):
    return x**2

# Integrate the function
result, error = quad(f, 0, 1)
print("Integral of f(x) from 0 to 1:", result)

# Plot the function
x = np.linspace(0, 1, 100)
y = f(x)
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function to Integrate")
plt.fill_between(x, 0, y, alpha=0.3)
plt.show()