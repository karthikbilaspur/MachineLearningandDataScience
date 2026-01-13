# Handling Categorical Data in Python
# 🤔 Categorical data is everywhere! Let's learn how to tame it 🐾.

# Why handle categorical data?
# - Many ML algorithms can't handle categorical data directly
# - Categorical data can be tricky to work with, but Python's got you covered 😊

# Popular techniques:
#   - One-Hot Encoding (OHE)
#   - Label Encoding
#   - Ordinal Encoding
#   - Binary Encoding
#   - Hashing

# Let's dive into examples 😎!

# One-Hot Encoding (OHE)
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Sample data
data = pd.DataFrame({'color': ['red', 'green', 'blue', 'red', 'green']})

# Apply OHE
encoder = OneHotEncoder(sparse=False)
encoded_data = encoder.fit_transform(data[['color']])
print(encoded_data)

# Label Encoding
from sklearn.preprocessing import LabelEncoder

# Sample data
data = pd.DataFrame({'color': ['red', 'green', 'blue', 'red', 'green']})

# Apply Label Encoding
le = LabelEncoder()
data['color_encoded'] = le.fit_transform(data['color'])
print(data)

# Ordinal Encoding
from sklearn.preprocessing import OrdinalEncoder

# Sample data
data = pd.DataFrame({'size': ['small', 'medium', 'large', 'small', 'medium']})

# Apply Ordinal Encoding
oe = OrdinalEncoder(categories=[['small', 'medium', 'large']])
data['size_encoded'] = oe.fit_transform(data[['size']])
print(data)

# Binary Encoding
import category_encoders as ce

# Sample data
data = pd.DataFrame({'color': ['red', 'green', 'blue', 'red', 'green']})

# Apply Binary Encoding
be = ce.BinaryEncoder(cols=['color'])
data_encoded = be.fit_transform(data)
print(data_encoded)

# Hashing
from sklearn.feature_extraction import FeatureHasher

# Sample data
data = [{'color': 'red'}, {'color': 'green'}, {'color': 'blue'}, {'color': 'red'}, {'color': 'green'}]

# Apply Hashing
h = FeatureHasher(n_features=3, input_type='string')
hashed_data = h.transform(data)
print(hashed_data.toarray())

# Choosing the right technique depends on your data and problem 😊.
# Want more examples or specific use cases? 🤔