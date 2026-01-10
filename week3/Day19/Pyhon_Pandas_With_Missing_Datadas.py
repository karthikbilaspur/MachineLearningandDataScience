"""
Working with Missing Data in Pandas
=====================================

In Pandas, missing data occurs when some values are missing or not collected properly.
These missing values are represented as:

*   None: A Python object used to represent missing values in object-type arrays.
*   NaN: A special floating-point value from NumPy which is recognized by all systems that use IEEE floating-point standards.
"""

import pandas as pd
import numpy as np

# Creating a DataFrame with missing values
data = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}
df = pd.DataFrame(data)

# Checking Missing Values
# ------------------------

# 1. Using isnull()
print(df.isnull())
# Output:
#    First Score  Second Score  Third Score
# 0         False         False         True
# 1         False         False        False
# 2          True         False        False
# 3         False          True        False

# 2. Using isna()
print(df.isna())
# Output:
#    First Score  Second Score  Third Score
# 0         False         False         True
# 1         False         False        False
# 2          True         False        False
# 3         False          True        False

# 3. Checking for Non-Missing Values Using notnull()
print(df.notnull())
# Output:
#    First Score  Second Score  Third Score
# 0          True          True        False
# 1          True          True         True
# 2         False          True         True
# 3          True         False         True

# Filling Missing Values
# ----------------------

# 1. Using fillna()
print(df.fillna(0))
# Output:
#    First Score  Second Score  Third Score
# 0        100.0          30.0         0.0
3.0         0.0
# 1         90.0         45.0        40.0
# 2          0.0         56.0        80.0
# 3         95.0          0.0        98.0

# 2. Using fillna() with method='pad'
print(df.fillna(method='pad'))
# Output:
#    First Score  Second Score  Third Score
# 0        100.0         30.0         NaN
# 1         90.0         45.0        40.0
# 2         90.0         56.0        80.0
# 3         95.0         56.0        98.0

# 3. Using fillna() with method='bfill'
print(df.fillna(method='bfill'))
# Output:
#    First Score  Second Score  Third Score
# 0        100.0         30.0        40.0
# 1         90.0         45.0        40.0
# 2         90.0         56.0        80.0
# 3         95.0          NaN        98.0

# 4. Using replace()
print(df.replace(to_replace=np.nan, value=-99))
# Output:
#    First Score  Second Score  Third Score
# 0        100.0         30.0       -99.0
# 1         90.0         45.0        40.0
# 2        -99.0         56.0        80.0
# 3         95.0       -99.0        98.0

# 5. Using interpolate()
df_interpolated = pd.DataFrame({"A": [12, 4, 5, None, 1],
                                "B": [None, 2, 54, 3, None],
                                "C": [20, 16, None, 3, 8],
                                "D": [14, 3, None, None, 6]})
print(df_interpolated.interpolate(method='linear', limit_direction='forward'))
# Output:
#      A     B     C     D
# 0  12.0   NaN  20.0  14.0
# 1   4.0   2.0  16.0   3.0
# 2   5.0  54.0  13.5   5.0
# 3   3.0   3.0   8.0   5.5
# 4   1.0   NaN   8.0   6.0

# Dropping Missing Values
# ------------------------

# 1. Dropping Rows with At Least One Null Value
print(df.dropna())
# Output:
#    First Score  Second Score  Third Score
# 1         90.0         45.0        40.0

# 2. Dropping Rows with All Null Values
print(df.dropna(how='all'))
# Output:
#    First Score  Second Score  Third Score
# 0        100.0         30.0         NaN
# 1         90.0         45.0        40.0
# 2          NaN         56.0        80.0
# 3         95.0          NaN        98.0

# 3. Dropping Columns with At Least One Null Value
print(df.dropna(axis=1))
# Output:
# Empty DataFrame
# Columns: []
# Index: [0, 1, 2, 3]