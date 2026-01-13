# random_forest.py

"""
Random Forest is a machine learning algorithm that uses many decision trees to make better predictions.
Each tree looks at different random parts of the data and their results are combined by voting for classification or averaging for regression,
making it an ensemble learning technique. This helps in improving accuracy and reducing errors.
"""

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

def main():
    # Implementing Random Forest for Classification Tasks
    print("# Implementing Random Forest for Classification Tasks")
    titanic_data = pd.read_csv('titanic.csv')
    titanic_data = titanic_data.dropna(subset=['Survived'])
    X = titanic_data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]
    y = titanic_data['Survived']
    X['Sex'] = X['Sex'].map({'female': 0, 'male': 1})
    X['Age'] = X['Age'].fillna(X['Age'].median())
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_classifier.fit(X_train, y_train)
    y_pred = rf_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    classification_rep = classification_report(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
    print("\nClassification Report:\n", classification_rep)
    sample = X_test.iloc[0:1]
    prediction = rf_classifier.predict(sample)
    sample_dict = sample.iloc[0].to_dict()
    print(f"\nSample Passenger: {sample_dict}")
    print(f"Predicted Survival: {'Survived' if prediction[0] == 1 else 'Did Not Survive'}")

    # Implementing Random Forest for Regression Tasks
    print("\n# Implementing Random Forest for Regression Tasks")
    california_housing = pd.read_csv('california_housing.csv')
    X = california_housing.drop('MEDV', axis=1)
    y = california_housing['MEDV']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_regressor.fit(X_train, y_train)
    y_pred = rf_regressor.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    single_data = X_test.iloc[0].values.reshape(1, -1)
    predicted_value = rf_regressor.predict(single_data)
    print(f"Predicted Value: {predicted_value[0]:.2f}")
    print(f"Actual Value: {y_test.iloc[0]:.2f}")
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R-squared Score: {r2:.2f}")

    # Advantages of Random Forest
    print("\n# Advantages of Random Forest")
    print("* Provides very accurate predictions even with large datasets.")
    print("* Handles missing data well without compromising accuracy.")
    print("* Doesn't require normalization or standardization on dataset.")
    print("* Reduces the risk of overfitting when combining multiple decision trees.")

    # Limitations of Random Forest
    print("\n# Limitations of Random Forest")
    print("* Can be computationally expensive especially with a large number of trees.")
    print("* It's harder to interpret the model compared to simpler models like decision trees.")

if __name__ == "__main__":
    main()