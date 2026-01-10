# chain_rule.py

"""
Chain Rule in Machine Learning
The chain rule is a fundamental concept in calculus that is widely used in machine learning, 
particularly in the context of neural networks. It is used to compute the derivative of a composite 
function, which is a function that is composed of multiple simpler functions.

Mathematical Definition
Given two functions f(x) and g(x), the chain rule states that the derivative of the composite 
function h(x) = f(g(x)) is given by:
h'(x) = f'(g(x)) * g'(x)

Application in Machine Learning
In machine learning, the chain rule is used to compute the gradients of the loss function with 
respect to the model's parameters. This is a crucial step in training neural networks, as it allows us 
to update the parameters to minimize the loss.

Here's an example of how the chain rule is applied in a simple neural network:
Let's say we have a neural network with two layers: an input layer x, a hidden layer h, and an output 
layer y. The forward pass is defined as:
h = sigmoid(W1 * x + b1)
y = sigmoid(W2 * h + b2)
where W1 and W2 are the weights, b1 and b2 are the biases, and sigmoid is the activation function.

To compute the gradient of the loss function L with respect to the weights W1, we can apply the chain rule:
dL/dW1 = dL/dy * dy/dh * dh/dW1
where dL/dy is the derivative of the loss function with respect to the output y, dy/dh is the derivative 
of the output y with respect to the hidden layer h, and dh/dW1 is the derivative of the hidden layer h 
with respect to the weights W1.
"""

import numpy as np

def sigmoid(x: float) -> float:
    """Sigmoid activation function"""
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x: float) -> float:
    """Derivative of sigmoid activation function"""
    return x * (1 - x)

class NeuralNetwork:
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int):
        self.W1 = np.random.rand(input_dim, hidden_dim)
        self.b1 = np.random.rand(hidden_dim)
        self.W2 = np.random.rand(hidden_dim, output_dim)
        self.b2 = np.random.rand(output_dim)

    def forward_pass(self, x: float -> float
        self.h = sigmoid(np.dot(x, self.W1) + self.b1)
        self.y_pred = sigmoid(np.dot(self.h, self.W2) + self.b2)
        return self.y_pred

    def compute_loss(self, y: np.ndarray) -> float:
        return np.mean((self.y_pred - y) ** 2)

    def backward_pass(self, x, y):
        dL_dy = 2 * (self.y_pred - y)
        dy_dh = sigmoid_derivative(self.y_pred)
        dh_dW1 = x[:, None] * sigmoid_derivative(self.h)[None, :]

        dL_dW1 = np.dot(dL_dy, dy_dh) * np.dot(dh_dW1, self.W2.T)
        dL_dW2 = np.dot(self.h.T, dL_dy * dy_dh)

        return dL_dW1, dL_dW2

def main():
    # Define the neural network
    input_dim = 2
    hidden_dim = 2
    output_dim = 1
    nn = NeuralNetwork(input_dim, hidden_dim, output_dim)

    # Define the input and output
    x = np.array([1, 2])
    y = np.array([3])

    # Forward pass
    y_pred = nn.forward_pass(x)

    # Compute the loss
    loss = nn.compute_loss(y)
    print("Loss:", loss)

    # Backward pass
    dL_dW1, dL_dW2 = nn.backward_pass(x, y)
    print("Gradient of W1:\n", dL_dW1)
    print("Gradient of W2:\n", dL_dW2)

if __name__ == "__main__"
 main()