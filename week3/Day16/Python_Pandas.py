"""
Python Pandas
=============

Pandas is a powerful library for data manipulation and analysis in Python.
"""

# History of Pandas
# ----------------
# Pandas was created by Wes McKinney in 2008, building on earlier work by others.

# What is Pandas?
# ----------------
# Pandas provides data structures and functions to efficiently handle structured data, including tabular data such as spreadsheets and SQL tables.

import pandas as pd

# Pandas Data Structures
# ----------------------

# 1. **Series**: A one-dimensional labeled array of values.
series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(series)
# Output:
# a    1
# b    2
# c    3
# d    4
# e    5
# dtype: int64

# 2. **DataFrame**: A two-dimensional labeled data structure with columns of potentially different types.
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'City': ['New York', 'Paris', 'Tokyo', 'Sydney']}
df = pd.DataFrame(data)
print(df)
# Output:
#     Name  Age       City
# 0   John   28  New York
# 1   Anna   24     Paris
# 2  Peter   35     Tokyo
# 3  Linda   32    Sydney

# Types of Pandas Data
# --------------------

# 1. **Numeric Data**: integer, float, etc.
# 2. **String Data**: object, category, etc.
# 3. **Date and Time Data**: datetime, timedelta, etc.
# 4. **Boolean Data**: bool, etc.

# Examples
# --------

# 1. **Reading CSV Files**
# df = pd.read_csv('data.csv')

# 2. **Writing to CSV Files**
# df.to_csv('data.csv', index=False)

# 3. **Data Cleaning and Preprocessing**
# df.dropna()  # drop rows with missing values
# df.fillna(0)  # fill missing values with 0

# 4. **Data Grouping and Aggregation**
# df.groupby('City')['Age'].mean()  # group by City and calculate mean Age

# Related Python Libraries
# -----------------------

# 1. **NumPy**: for numerical computations
# 2. **Matplotlib** and **Seaborn**: for data visualization
# 3. **Scikit-learn**: for machine learning
# 4. **Statsmodels**: for statistical modeling

# Example: Using Pandas with Matplotlib
import matplotlib.pyplot as plt
df['Age'].plot.hist()
plt.show()