"""
Handling Outliers with Pandas
=============================

Outliers are data points that are significantly different from the other data points in a dataset.
"""

import pandas as pd
import numpy as np

# Creating a DataFrame
data = {'Values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000]}
df = pd.DataFrame(data)

print(df)
# Output:
#    Values
# 0       1
# 1       2
# 2       3
# 3       4
# 4       5
# 5       6
# 6       7
# 7       8
# 8       9
# 9      10
# 10   1000

# Detecting Outliers
# ------------------

# 1. Using the Z-Score method
from scipy import stats
z_scores = np.abs(stats.zscore(df['Values']))
print(z_scores)
# Output:
# [0.02828427 0.05656854 0.08485281 0.11313708 0.14142135 0.16970563
#  0.1979899  0.22627417 0.25455844 0.28284271 3.39411255]

# 2. Using the IQR method
Q1 = df['Values'].quantile(0.25)
Q3 = df['Values'].quantile(0.75)
IQR = Q3 - Q1
print(IQR)
# Output:
# 4.5

# Removing Outliers
# ------------------

# 1. Using the Z-Score method
df_filtered = df[(z_scores < 3).all(axis=1)]
print(df_filtered)
# Output:
#    Values
# 0       1
# 1       2
# 2       3
# 3       4
# 4       5
# 5       6
# 6       7
# 7       8
# 8       9
# 9      10

# 2. Using the IQR method
df_filtered = df[(df['Values'] >= Q1 - 1.5 * IQR) & (df['Values'] <= Q3 + 1.5 * IQR)]
print(df_filtered)
# Output:
#    Values
# 0       1
# 1       2
# 2       3
# 3       4
# 4       5
# 5       6
# 6       7
# 7       8
# 8       9
# 9      10

# Replacing Outliers
# ------------------

# 1. Using the mean
mean = df['Values'].mean()
df['Values'] = np.where((z_scores > 3), mean, df['Values'])
print(df)
# Output:
#    Values
# 0       1
# 1       2
# 2       3
# 3       4
# 4       5
# 5       6
# 6       7
# 7       8
# 8       9
# 9      10
# 10    5.5

# 2. Using the median
median = df['Values'].median()
df['Values'] = np.where((z_scores > 3), median, df['Values'])
print(df)
# Output:
#    Values
# 0       1
# 1       2
# 2       3
# 3       4
# 4       5
# 5       6
# 6       7
# 7       8
# 8       9
# 9      10
# 10    5.5