"""
What is Random Forest Classifier?
Random Forest is a supervised learning algorithm that combines multiple decision trees to predict categorical outcomes.

Key Characteristics:
- Handles large datasets and high-dimensional data
- Reduces overfitting by combining predictions from multiple trees
- Robust to noisy data and works well with categorical data

Implementation Steps:
1. Import libraries: pandas, matplotlib, seaborn, sklearn
2. Load Iris dataset
3. Prepare data: separate features (X) and target variable (y)
4. Split data: train (80%) and test (20%) sets
5. Feature scaling (optional): StandardScaler
6. Build model: RandomForestClassifier(n_estimators=100, random_state=42)
7. Train model: fit(X_train, y_train)
8. Make predictions: predict(X_test)
9. Evaluate model: accuracy score, confusion matrix
10. Feature importance: plot feature_importances_

Example Code:
"""

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

def main():
    # Load Iris dataset
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target

    # Prepare data
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Feature scaling
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Build model
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Make predictions
    y_pred = clf.predict(X_test)

    # Evaluate model
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy * 100:.2f}%')

    # Confusion matrix
    conf_matrix = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt='g', cmap='Blues', cbar=False, 
                xticklabels=iris.target_names, yticklabels=iris.target_names)
    plt.title('Confusion Matrix Heatmap')
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
    plt.show()

    # Feature importance
    feature_importances = clf.feature_importances_
    plt.barh(iris.feature_names, feature_importances)
    plt.xlabel('Feature Importance')
    plt.title('Feature Importance in Random Forest Classifier')
    plt.show()

if __name__ == "__main__":
    main()