"""
Data Duplication in Pandas
==========================

Data duplication occurs when there are duplicate rows in a DataFrame.
"""

import pandas as pd

# Creating a DataFrame with duplicate rows
data = {'Name': ['John', 'Anna', 'John', 'Anna', 'Peter'],
        'Age': [28, 24, 28, 24, 35],
        'City': ['New York', 'Paris', 'New York', 'Paris', 'Tokyo']}
df = pd.DataFrame(data)

print(df)
# Output:
#     Name  Age       City
# 0   John   28  New York
# 1   Anna   24     Paris
# 2   John   28  New York
# 3   Anna   24     Paris
# 4  Peter   35     Tokyo

# Checking for Duplicate Rows
# ---------------------------

print(df.duplicated())
# Output:
# 0    False
# 1    False
# 2     True
# 3     True
# 4    False
# dtype: bool

# Removing Duplicate Rows
# -----------------------

# 1. Using drop_duplicates()
df_unique = df.drop_duplicates()
print(df_unique)
# Output:
#     Name  Age       City
# 0   John   28  New York
# 1   Anna   24     Paris
# 4  Peter   35     Tokyo

# 2. Using drop_duplicates() with subset
df_unique = df.drop_duplicates(subset=['Name', 'Age'])
print(df_unique)
# Output:
#     Name  Age       City
# 0   John   28  New York
# 1   Anna   24     Paris
# 4  Peter   35     Tokyo

# 3. Using drop_duplicates() with keep='last'
df_unique = df.drop_duplicates(keep='last')
print(df_unique)
# Output:
#     Name  Age       City
# 2   John   28  New York
# 3   Anna   24     Paris
# 4  Peter   35     Tokyo

# Removing Duplicate Rows from a CSV File
# --------------------------------------

# df = pd.read_csv('data.csv')
# df_unique = df.drop_duplicates()
# df_unique.to_csv('data_unique.csv', index=False)

# Example Use Case
# ----------------

# Create a sample DataFrame
data = {'ID': [1, 2, 2, 3, 4, 4],
        'Name': ['John', 'Anna', 'Anna', 'Peter', 'Linda', 'Linda'],
        'Age': [28, 24, 24, 35, 32, 32]}
df = pd.DataFrame(data)

# Remove duplicate rows
df_unique = df.drop_duplicates()

print(df_unique)
# Output:
#    ID   Name  Age
# 0   1   John   28
# 1   2   Anna   24
# 3   3  Peter   35
# 4   4  Linda   32