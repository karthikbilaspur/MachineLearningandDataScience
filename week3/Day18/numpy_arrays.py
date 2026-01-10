"""
NumPy Arrays
===============

NumPy (Numerical Python) is a library for working with arrays and mathematical operations in Python.
"""

# History of NumPy
# ----------------
# NumPy was created by Travis Oliphant in 2005, building on earlier work by Jim Hugunin and others.

# What are NumPy Arrays?
# ------------------------
# NumPy arrays are multi-dimensional collections of values of the same data type.

import numpy as np

# Example 1: Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # Output: [1 2 3 4 5]

# Example 2: Creating a 2D NumPy array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)
# Output:
# [[1 2 3]
#  [4 5 6]]

# Types of NumPy Arrays
# ----------------------
# NumPy arrays can be of various types, including:

# 1. **Integer arrays**: arrays of integers
int_arr = np.array([1, 2, 3], dtype=np.int32)
print(int_arr.dtype)  # Output: int32

# 2. **Float arrays**: arrays of floating-point numbers
float_arr = np.array([1.0, 2.0, 3.0], dtype=np.float64)
print(float_arr.dtype)  # Output: float64

# 3. **Complex arrays**: arrays of complex numbers
complex_arr = np.array([1+2j, 2+3j, 3+4j], dtype=np.complex128)
print(complex_arr.dtype)  # Output: complex128

# 4. **Boolean arrays**: arrays of boolean values
bool_arr = np.array([True, False, True], dtype=np.bool_)
print(bool_arr.dtype)  # Output: bool

# 5. **String arrays**: arrays of strings
str_arr = np.array(['hello', 'world'], dtype=np.object_)
print(str_arr.dtype)  # Output: object