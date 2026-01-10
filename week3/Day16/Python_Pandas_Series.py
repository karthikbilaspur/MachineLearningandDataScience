"""
Python Pandas Series
====================

A Series is a one-dimensional labeled array of values in Pandas.
"""

import pandas as pd

# Creating a Series
# -----------------

# 1. **From a list**
series1 = pd.Series([1, 2, 3, 4, 5])
print(series1)
# Output:
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

# 2. **From a numpy array**
import numpy as np
series2 = pd.Series(np.array([1, 2, 3, 4, 5]))
print(series2)
# Output:
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

# 3. **From a dictionary**
series3 = pd.Series({'a': 1, 'b': 2, 'c': 3})
print(series3)
# Output:
# a    1
# b    2
# c    3
# dtype: int64

# Series Attributes
# -----------------

# 1. **index**: The index (labels) of the Series.
print(series1.index)  # Output: RangeIndex(start=0, stop=5, step=1)

# 2. **values**: The values of the Series.
print(series1.values)  # Output: [1 2 3 4 5]

# 3. **dtype**: The data type of the Series.
print(series1.dtype)  # Output: int64

# Series Methods
# ----------------

# 1. **add()**: Element-wise addition.
series4 = series1.add([1, 2, 3, 4, 5])
print(series4)
# Output:
# 0     2
# 1     4
# 2     6
# 3     8
# 4    10
# dtype: int64

# 2. **sub()**: Element-wise subtraction.
series5 = series1.sub([1, 2, 3, 4, 5])
print(series5)
# Output:
# 0     0
# 1     0
# 2     0
# 3     0
# 4     0
# dtype: int64

# 3. **mul()**: Element-wise multiplication.
series6 = series1.mul([1, 2, 3, 4, 5])
print(series6)
# Output:
# 0      1
# 1      4
# 2      9
# 3     16
# 4     25
# dtype: int64

# 4. **div()**: Element-wise division.
series7 = series1.div([1, 2, 3, 4, 5])
print(series7)
# Output:
# 0    1.000000
# 1    1.000000
# 2    1.000000
# 3    1.000000
# 4    1.000000
# dtype: float64

# Indexing and Slicing
# --------------------

# 1. **Label-based indexing**
series8 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(series8['b'])  # Output: 2

# 2. **Position-based indexing**
print(series8.iloc[1])  # Output: 2

# 3. **Slicing**
print(series8['b':'d'])
# Output:
# b    2
# c    3
# d    4
# dtype: int64