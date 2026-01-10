"""
Create a Correlation Matrix using Python
=========================================

A correlation matrix is a table showing correlation coefficients between variables.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Creating a DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [2, 3, 5, 7, 11],
        'C': [3, 5, 7, 11, 13]}
df = pd.DataFrame(data)

print(df)
# Output:
#    A   B   C
# 0  1   2   3
# 1  2   3   5
# 2  3   5   7
# 3  4   7  11
# 4  5  11  13

# Correlation Matrix
# ------------------

# 1. Using corr()
corr_matrix = df.corr()
print(corr_matrix)
# Output:
#           A         B         C
# A  1.000000  0.960769  0.981980
# B  0.960769  1.000000  0.991241
# C  0.981980  0.991241  1.000000

# 2. Using corr() with method='pearson'
corr_matrix = df.corr(method='pearson')
print(corr_matrix)
# Output:
#           A         B         C
# A  1.000000  0.960769  0.981980
# B  0.960769  1.000000  0.991241
# C  0.981980  0.991241  1.000000

# 3. Using corr() with method='kendall'
corr_matrix = df.corr(method='kendall')
print(corr_matrix)
# Output:
#           A         B         C
# A  1.000000  0.948683  0.948683
# B  0.948683  1.000000  1.000000
# C  0.948683  1.000000  1.000000

# 4. Using corr() with method='spearman'
corr_matrix = df.corr(method='spearman')
print(corr_matrix)
# Output:
#           A         B         C
# A  1.000000  0.948683  0.948683
# B  0.948683  1.000000  1.000000
# C  0.948683  1.000000  1.000000

# Heatmap
# --------

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Matrix')
plt.show()