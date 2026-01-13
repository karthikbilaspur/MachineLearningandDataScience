import numpy as np
import matplotlib.pyplot as plt

# Gradient Descent function for Linear Regression
def gradient_descent(X, y, learning_rate=0.01, num_iterations=1000):
    # Initialize coefficients (weights) with zeros
    weights = np.zeros(X.shape[1])
    bias = 0
    
    # Store cost (MSE) at each iteration
    costs = []
    
    # Perform Gradient Descent
    for _ in range(num_iterations):
        # Predict output
        predictions = np.dot(X, weights) + bias
        
        # Calculate error
        errors = predictions - y
        
        # Calculate gradients
        weight_gradients = (2/X.shape[0]) * np.dot(X.T, errors)
        bias_gradient = (2/X.shape[0]) * np.sum(errors)
        
        # Update weights and bias
        weights -= learning_rate * weight_gradients
        bias -= learning_rate * bias_gradient
        
        # Calculate cost (MSE)
        cost = np.mean(errors**2)
        costs.append(cost)
    
    return weights, bias, costs

# Sample dataset
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([3, 5, 7, 9])

# Add a column of ones for bias term
X = np.c_[np.ones(X.shape[0]), X]

# Run Gradient Descent
weights, bias, costs = gradient_descent(X, y)

print(f"Weights: {weights}, Bias: {bias}")

# Plot cost vs iterations
plt.plot(costs)
plt.xlabel('Iterations')
plt.ylabel('Cost (MSE)')
plt.show()