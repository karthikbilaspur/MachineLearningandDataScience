"""
Python Pandas CRUD Operations
=============================

CRUD (Create, Read, Update, Delete) operations in Pandas DataFrame.
"""

import pandas as pd

# Create a DataFrame
# ------------------

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

# Create a new row
# ----------------

new_row = pd.DataFrame({'Name': ['Mike'], 'Age': [30], 'City': ['London']})
df = pd.concat([df, new_row], ignore_index=True)
print(df)
# Output:
#     Name  Age       City
# 0   John   28  New York
# 1   Anna   24     Paris
# 2  Peter   35     Tokyo
# 3  Linda   32    Sydney
# 4   Mike   30    London

# Read data
# ---------

# Read a specific row
print(df.loc[0])
# Output:
# Name       John
# Age         28
# City    New York
# Name: 0, dtype: object

# Read a specific column
print(df['Name'])
# Output:
# 0      John
# 1      Anna
# 2     Peter
# 3     Linda
# 4      Mike
# Name: Name, dtype: object

# Update data
# ----------

# Update a specific cell
df.loc[0, 'Name'] = 'Jonathan'
print(df)
# Output:
#       Name  Age       City
# 0  Jonathan   28  New York
# 1      Anna   24     Paris
# 2     Peter   35     Tokyo
# 3     Linda   32    Sydney
# 4      Mike   30    London

# Update a specific row
df.loc[1] = ['Ann', 25, 'Rome']
print(df)
# Output:
#       Name  Age       City
# 0  Jonathan   28  New York
# 1       Ann   25      Rome
# 2     Peter   35     Tokyo
# 3     Linda   32    Sydney
# 4      Mike   30    London

# Delete data
# ----------

# Delete a specific row
df = df.drop(0)
print(df)
# Output:
#    Name  Age     City
# 1   Ann   25     Rome
# 2  Peter   35    Tokyo
# 3  Linda   32   Sydney
# 4   Mike   30   London

# Delete a specific column
df = df.drop('Age', axis=1)
print(df)
# Output:
#    Name     City
# 1   Ann     Rome
# 2  Peter    Tokyo
# 3  Linda   Sydney
# 4   Mike   London