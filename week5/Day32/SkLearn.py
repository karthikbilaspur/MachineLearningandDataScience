# Import necessary libraries for machine learning tasks
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np

# Load the Iris dataset, a classic multiclass classification problem
iris = load_iris()
X = iris.data  # Features (input variables)
y = iris.target  # Target variable (output labels)

# Print feature and target names for better understanding
feature_names = iris.feature_names
target_names = iris.target_names
print("Feature names:", feature_names)
print("Target names:", target_names)

# Split the dataset into training and testing sets (60% for training, 40% for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

# Print shapes of the split data to ensure correct proportions
print("X_train Shape:", X_train.shape)
print("X_test Shape:", X_test.shape)
print("Y_train Shape:", y_train.shape)
print("Y_test Shape:", y_test.shape)

# Demonstrate handling categorical data using Label Encoding
categorical_feature = ['cat', 'dog', 'dog', 'cat', 'bird']
encoder = LabelEncoder()
encoded_feature = encoder.fit_transform(categorical_feature)
print("Encoded feature (Label Encoding):", encoded_feature)

# Demonstrate handling categorical data using One-Hot Encoding
categorical_feature = np.array(categorical_feature).reshape(-1, 1)
encoder = OneHotEncoder(sparse_output=False)
encoded_feature = encoder.fit_transform(categorical_feature)
print("Encoded feature (One-Hot Encoding):\n", encoded_feature)

# Train a Logistic Regression model on the training data
log_reg = LogisticRegression(max_iter=200)  # Create a logistic regression classifier
log_reg.fit(X_train, y_train)  # Train the model on the training data

# Make predictions on the test data
y_pred = log_reg.predict(X_test)

# Evaluate the model's accuracy
print("Logistic Regression model accuracy:", metrics.accuracy_score(y_test, y_pred))

# Make predictions on new sample data
sample = [[3, 5, 4, 2], [2, 3, 5, 4]]
preds = log_reg.predict(sample)
pred_species = [iris.target_names[p] for p in preds]
print("Predictions:", pred_species)