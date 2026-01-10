# jacobian_hessian.py

"""
Jacobian and Hessian Matrices
================================

In mathematics, the Jacobian matrix and Hessian matrix are used to describe the behavior of a 
multivariate function.

Jacobian Matrix
----------------

The Jacobian matrix is a matrix of partial derivatives of a vector-valued function. It is used to 
describe the linear approximation of a function near a point.

Hessian Matrix
----------------

The Hessian matrix is a square matrix of second partial derivatives of a scalar-valued function. It 
is used to describe the curvature of a function near a point.

Python Implementation
---------------------

Here is an example implementation of Jacobian and Hessian matrices in Python:
"""

import numpy as np
import sympy as sp

# Define a function
x, y = sp.symbols('x y')
f = x**2 + 2*y**2

# Compute the Jacobian matrix
J = [sp.diff(f, x), sp.diff(f, y)]
print("Jacobian Matrix:")
print(J)

# Compute the Hessian matrix
H = [[sp.diff(f, x, x), sp.diff(f, x, y)], [sp.diff(f, y, x), sp.diff(f, y, y)]]
print("\nHessian Matrix:")
print(H)

# Define a multivariate function
def f(x, y):
    return x**2 + 2*y**2

# Compute the Jacobian matrix using NumPy
def jacobian(f: callable, x: float, y: float) -> float:
    eps = 1e-6
    J = np.array([
        [(f(x + eps, y) - f(x - eps, y)) / (2 * eps)],
        [(f(x, y + eps) - f(x, y - eps)) / (2 * eps)]
    ])
    return J

# Compute the Hessian matrix using NumPy
def hessian(f: callable, x: float, y: float) -> float:
    eps = 1e-6
    H = np.array([
        [(f(x + eps, y) - 2*f(x, y) + f(x - eps, y)) / eps**2, (f(x + eps, y + eps) - f(x + eps, y - eps) - f(x - eps, y + eps) + f(x - eps, y - eps)) / (4 * eps**2)],
        [(f(x + eps, y + eps) - f(x + eps, y - eps) - f(x - eps, y + eps) + f(x - eps, y - eps)) / (4 * eps**2), (f(x, y + eps) - 2*f(x, y) + f(x, y - eps)) / eps**2]
    ])
    return H

# Test the functions
x, y = 1, 2
print("\nJacobian Matrix (NumPy):")
print(jacobian(f, x, y))
print("\nHessian Matrix (NumPy):")
print(hessian(f, x, y))

# Using SymPy to compute Jacobian and Hessian matrices
x, y = sp.symbols('x y')
f = x**2 + 2*y**2
J = [sp.diff(f, x), sp.diff(f, y)]
H = [[sp.diff(f, x, x), sp.diff(f, x, y)], [sp.diff(f, y, x), sp.diff(f, y, y)]]
print("\nJacobian Matrix (SymPy):")
print(J)
print("\nHessian Matrix (SymPy):")
print(H)