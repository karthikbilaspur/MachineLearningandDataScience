
"""
NumPy Arithmetic Operations
==========================

NumPy provides various arithmetic operations that can be performed on arrays.
"""

import numpy as np

# Example arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# Basic Arithmetic Operations
# ---------------------------

# 1. **Addition**
add_result = np.add(arr1, arr2)
print("Addition:", add_result)  # Output: [ 7  9 11 13 15]

# 2. **Subtraction**
sub_result = np.subtract(arr1, arr2)
print("Subtraction:", sub_result)  # Output: [-5 -5 -5 -5 -5]

# 3. **Multiplication**
mul_result = np.multiply(arr1, arr2)
print("Multiplication:", mul_result)  # Output: [ 6 14 24 36 50]

# 4. **Division**
div_result = np.divide(arr1, arr2)
print("Division:", div_result)  # Output: [0.16666667 0.28571429 0.375      0.44444444 0.5       ]

# Element-wise Operations
# ----------------------

# You can also perform element-wise operations using operators
print("Element-wise Addition:", arr1 + arr2)  # Output: [ 7  9 11 13 15]
print("Element-wise Subtraction:", arr1 - arr2)  # Output: [-5 -5 -5 -5 -5]
print("Element-wise Multiplication:", arr1 * arr2)  # Output: [ 6 14 24 36 50]
print("Element-wise Division:", arr1 / arr2)  # Output: [0.16666667 0.28571429 0.375      0.44444444 0.5       ]

# Other Operations
# ----------------

# 1. **Exponentiation**
exp_result = np.exp(arr1)
print("Exponentiation:", exp_result)

# 2. **Square Root**
sqrt_result = np.sqrt(arr1)
print("Square Root:", sqrt_result)

# 3. **Logarithm**
log_result = np.log(arr1)
print("Logarithm:", log_result)
