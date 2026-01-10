"""
Pandas GroupBy
===============

The GroupBy function in Pandas is used to split the data into groups based on some criteria.
"""

import pandas as pd

# Creating a DataFrame
data = {'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Chicago'],
        'Year': [2020, 2020, 2020, 2021, 2021, 2021],
        'Sales': [100, 200, 300, 400, 500, 600]}
df = pd.DataFrame(data)

print(df)
# Output:
#           City  Year  Sales
# 0      New York  2020    100
# 1  Los Angeles  2020    200
# 2       Chicago  2020    300
# 3      New York  2021    400
# 4  Los Angeles  2021    500
# 5       Chicago  2021    600

# GroupBy Function
# ----------------

# 1. Grouping by a single column
grouped = df.groupby('City')
print(grouped.sum())
# Output:
#              Sales
# City             
# Chicago      900
# Los Angeles  700
# New York     500

# 2. Grouping by multiple columns
grouped = df.groupby(['City', 'Year'])
print(grouped.sum())
# Output:
#                      Sales
# City        Year       
# Chicago     2020    300
#             2021    600
# Los Angeles 2020    200
#             2021    500
# New York    2020    100
#             2021    400

# Aggregate Functions
# -------------------

# 1. sum()
print(df.groupby('City')['Sales'].sum())
# Output:
# City
# Chicago      900
# Los Angeles  700
# New York     500
# Name: Sales, dtype: int64

# 2. mean()
print(df.groupby('City')['Sales'].mean())
# Output:
# City
# Chicago      450.0
# Los Angeles  350.0
# New York     250.0
# Name: Sales, dtype: float64

# 3. count()
print(df.groupby('City')['Sales'].count())
# Output:
# City
# Chicago        2
# Los Angeles    2
# New York       2
# Name: Sales, dtype: int64

# 4. max()
print(df.groupby('City')['Sales'].max())
# Output:
# City
# Chicago      600
# Los Angeles  500
# New York     400
# Name: Sales, dtype: int64

# 5. min()
print(df.groupby('City')['Sales'].min())
# Output:
# City
# Chicago      300
# Los Angeles  200
# New York     100
# Name: Sales, dtype: int64

# Apply Function
# --------------

def custom_function(x):
    return x.max() - x.min()

print(df.groupby('City')['Sales'].apply(custom_function))
# Output:
# City
# Chicago      300
# Los Angeles  300
# New York     300
# Name: Sales, dtype: int64

# Transform Function
# ------------------

print(df.groupby('City')['Sales'].transform(lambda x: x - x.mean()))
# Output:
# 0   -150.0
# 1   -150.0
# 2   -150.0
# 3    150.0
# 4    150.0
# 5    150.0
# Name: Sales, dtype: float64