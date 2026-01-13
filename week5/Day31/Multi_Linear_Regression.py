import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample dataset
data = {'Feature1': [1, 2, 3, 4, 5],
        'Feature2': [2, 3, 4, 5, 6],
        'Target': [3, 5, 7, 9, 11]}
df = pd.DataFrame(data)

# Split data into features (X) and target (y)
X = df[['Feature1', 'Feature2']]
y = df['Target']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'MSE: {mse:.2f}')