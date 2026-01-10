"""
Python Pandas DataFrame
=======================

A DataFrame is a two-dimensional labeled data structure with columns of potentially different types in Pandas.
"""

import pandas as pd

# Creating a DataFrame
# --------------------

# 1. **From a dictionary**
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

# 2. **From a list of lists**
data = [['John', 28, 'New York'],
        ['Anna', 24, 'Paris'],
        ['Peter', 35, 'Tokyo'],
        ['Linda', 32, 'Sydney']]
df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)
# Output:
#     Name  Age       City
# 0   John   28  New York
# 1   Anna   24     Paris
# 2  Peter   35     Tokyo
# 3  Linda   32    Sydney

# DataFrame Attributes
# --------------------

# 1. **index**: The index (labels) of the DataFrame.
print(df.index)  # Output: RangeIndex(start=0, stop=4, step=1)

# 2. **columns**: The column labels of the DataFrame.
print(df.columns)  # Output: Index(['Name', 'Age', 'City'], dtype='object')

# 3. **values**: The values of the DataFrame.
print(df.values)
# Output:
# [['John' 28 'New York']
#  ['Anna' 24 'Paris']
#  ['Peter' 35 'Tokyo']
#  ['Linda' 32 'Sydney']]

# DataFrame Methods
# -----------------

# 1. **head()**: Return the first n rows.
print(df.head(2))
# Output:
#   Name  Age       City
# 0  John   28  New York
# 1  Anna   24     Paris

# 2. **tail()**: Return the last n rows.
print(df.tail(2))
# Output:
#     Name  Age     City
# 2  Peter   35    Tokyo
# 3  Linda   32   Sydney

# 3. **info()**: Print a concise summary of the DataFrame.
df.info()
# Output:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4 entries, 0 to 3
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype 
# ---  ------  --------------  ----- 
#  0   Name    4 non-null      object
#  1   Age     4 non-null      int64 
#  2   City    4 non-null      object
# dtypes: int64(1), object(2)
# memory usage: 224.0+ bytes

# 4. **describe()**: Generate descriptive statistics.
print(df.describe())
# Output:
#          Age
# count   4.000000
# mean   29.750000
# std     4.787136
# min    24.000000
# 25%    26.000000
# 50%    30.000000
# 75%    33.500000
# max    35.000000

# Indexing and Slicing
# --------------------

# 1. **Label-based indexing**
print(df.loc[0, 'Name'])  # Output: John

# 2. **Position-based indexing**
print(df.iloc[0, 0])  # Output: John

# 3. **Slicing**
print(df.loc[0:1, 'Name':'Age'])
# Output:
#   Name  Age
# 0  John   28
# 1  Anna   24

# Data Manipulation
# -----------------

# 1. **Adding a new column**
df['Country'] = ['USA', 'France', 'Japan', 'Australia']
print(df)
# Output:
#     Name  Age       City    Country
# 0   John   28  New York        USA
# 1   Anna   24     Paris      France
# 2  Peter   35     Tokyo       Japan
# 3  Linda   32    Sydney  Australia

# 2. **Dropping a column**
df = df.drop('Country', axis=1)
print(df)
# Output:
#     Name  Age       City
# 0   John   28  New York
# 1   Anna   24     Paris
# 2  Peter   35     Tokyo
# 3  Linda   32    Sydney