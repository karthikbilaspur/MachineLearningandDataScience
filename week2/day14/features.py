# feature_selection_f_anova.py

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def load_data():
    """
    Load Iris dataset.

    Returns:
    tuple: Features and target variable
    """
    data = load_iris()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target)
    return X, y

def split_data(X, y):
    """
    Split dataset into training and testing sets.

    Parameters:
    X (pd.DataFrame): Features
    y (pd.Series): Target variable

    Returns:
    tuple: Training and testing sets
    """
    return train_test_split(X, y, test_size=0.3, random_state=42)

def select_features(X_train, y_train, k):
    """
    Select top k features using F-ANOVA.

    Parameters:
    X_train (pd.DataFrame): Training features
    y_train (pd.Series): Training target variable
    k (int): Number of top features to select

    Returns:
    tuple: Selected features and their scores
    """
    selector = SelectKBest(score_func=f_classif, k=k)
    X_train_selected = selector.fit_transform(X_train, y_train)
    selected_features = X_train.columns[selector.get_support()]
    f_scores = selector.scores_[selector.get_support()]
    return selected_features, f_scores

def train_model(X_train_selected, y_train, X_test_selected, y_test):
    """
    Train Random Forest classifier and evaluate its accuracy.

    Parameters:
    X_train_selected (pd.DataFrame): Selected training features
    y_train (pd.Series): Training target variable
    X_test_selected (pd.DataFrame): Selected testing features
    y_test (pd.Series): Testing target variable
    """
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train_selected, y_train)
    y_pred = model.predict(X_test_selected)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy of the model with selected features: {accuracy:.4f}")

def main():
    # Load dataset
    X, y = load_data()

    # Split dataset
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Select top features using F-ANOVA
    k = 2
    selected_features, f_scores = select_features(X_train, y_train, k)
    print(f"Selected Features: {selected_features}")
    print(f"F-Scores: {f_scores}")

    # Transform selected features
    selector = SelectKBest(score_func=f_classif, k=k)
    X_train_selected = selector.fit_transform(X_train, y_train)
    X_test_selected = selector.transform(X_test)

    # Train model and evaluate accuracy
    train_model(X_train_selected, y_train, X_test_selected, y_test)

if __name__ == "__main__":
    main()