
# feature_selection_chi_square.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import chi2, SelectKBest

def load_data(file_path):
    """
    Load dataset from CSV file.

    Parameters:
    file_path (str): Path to CSV file

    Returns:
    pd.DataFrame: Loaded dataset
    """
    return pd.read_csv(file_path)

def clean_data(df: pd.DataFrame):
    """
    Clean dataset by removing missing values.

    Parameters:
    df (pd.DataFrame): Dataset to clean

    Returns:
    pd.DataFrame: Cleaned dataset
    """
    print(df.isnull().sum())
    df = df.dropna()
    print(df.isnull().sum())
    return df

def encode_features(df: pd.DataFrame, categorical_features: list, target_variable: str) -> pd.DataFrame:
    """
    Encode categorical features using LabelEncoder.

    Parameters:
    df (pd.DataFrame): Dataset
    categorical_features (list): List of categorical feature names
    target_variable (str): Name of target variable

    Returns:
    pd.DataFrame: Dataset with encoded features
    """
    le = LabelEncoder()
    for feature in categorical_features:
        df[feature] = le.fit_transform(df[feature])
    df[target_variable] = le.fit_transform(df[target_variable])
    return df

def select_features(df: pd.DataFrame, categorical_features: list, target_variable: str, k: int):
    """
    Select top k features using Chi-Square Test.

    Parameters:
    df (pd.DataFrame): Dataset
    categorical_features (list): List of categorical feature names
    target_variable (str): Name of target variable
    k (int): Number of top features to select

    Returns:
    tuple: Selected features and their scores
    """
    X = df[categorical_features]
    y = df[target_variable]
    selector = SelectKBest(score_func=chi2, k=k)
    X_new = selector.fit_transform(X, y)
    feature_scores = selector.scores_
    selected_features = X.columns[selector.get_support()]
    return selected_features, feature_scores

def main():
    # Load dataset
    df = load_data('customer_purchase_behavior.csv')

    # Clean dataset
    df = clean_data(df)

    # Encode features
    categorical_features = ['Gender', 'Age', 'AnnualIncome', 'ProductCategory']
    target_variable = 'PurchaseStatus'
    df = encode_features(df, categorical_features, target_variable)

    # Select top features using Chi-Square Test
    k = 2
    selected_features, feature_scores = select_features(df, categorical_features, target_variable, k)
    print("Selected Features:", selected_features)
    print("Feature Scores:", feature_scores)

if __name__ == "__main__":
    main()