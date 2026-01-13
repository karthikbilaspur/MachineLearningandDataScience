import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset (replace with your own dataset)
data = pd.read_csv('rainfall_data.csv')

# Split data into features (X) and target (y)
X = data[['JAN', 'FEB', 'MAR', 'APR', 'MAY']]
y = data['ANNUAL']

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