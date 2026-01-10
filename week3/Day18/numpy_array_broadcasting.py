"""
NumPy Array Broadcasting
=======================

NumPy's broadcasting feature allows you to perform operations on arrays with different shapes and sizes.
"""

import numpy as np

# Example arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10])

# Broadcasting Example 1: Scalar Broadcasting
# -------------------------------------------

# When you perform an operation between an array and a scalar, NumPy broadcasts the scalar to the shape of the array
result1 = arr1 + arr2
print("Broadcasting Result 1:", result1)  # Output: [11 12 13 14 15]

# Broadcasting Example 2: Array Broadcasting
# -----------------------------------------

# When you perform an operation between two arrays, NumPy broadcasts the smaller array to the shape of the larger array
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4 = np.array([10, 20, 30])
result2 = arr3 + arr4
print("Broadcasting Result 2:")
print(result2)
# Output:
# [[11 22 33]
#  [14 25 36]]

# Broadcasting Rules
# -----------------

# 1. **Matching Dimensions**: NumPy compares the shapes of the arrays from right to left.
# 2. **Size 1 Dimensions**: If one array has a size 1 dimension, it can be broadcasted to match the other array.
# 3. **Missing Dimensions**: If one array is missing dimensions, it is padded with size 1 dimensions.

# Example: Broadcasting with 2D Arrays
arr5 = np.array([[1, 2], [3, 4]])
arr6 = np.array([10, 20])
result3 = arr5 + arr6
print("Broadcasting Result 3:")
print(result3)
# Output:
# [[11 22]
#  [13 24]]

# Example: Broadcasting with 3D Arrays
arr7 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
arr8 = np.array([10, 20])
result4 = arr7 + arr8
print("Broadcasting Result 4:")
print(result4)
# Output:
# [[[11 22]
#   [13 24]]
#  [[15 26]
#   [17 28]]]