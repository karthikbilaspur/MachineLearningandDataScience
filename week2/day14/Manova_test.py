# manova_test.py

import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.multivariate.manova import MANOVA

def generate_data(num_samples):
    """
    Generate random data for MANOVA test.

    Parameters:
    num_samples (int): Number of samples.

    Returns:
    X (pd.DataFrame): Independent features.
    Y (pd.DataFrame): Dependent variables.
    """
    np.random.seed(42)
    X = pd.DataFrame({
        'feature1': np.random.normal(10, 2, num_samples),
        'feature2': np.random.normal(20, 5, num_samples),
        'feature3': np.random.normal(30, 10, num_samples),
        'feature4': np.random.normal(40, 15, num_samples),
        'feature5': np.random.normal(50, 20, num_samples), 
        'feature6': np.random.normal(15, 20, num_samples)
    })

    Y = pd.DataFrame({
        'target1': 0.5 * X['feature1'] + 0.2 * X['feature2'] + np.random.normal(0, 1, num_samples),
        'target2': 0.3 * X['feature3'] + 0.1 * X['feature4'] + np.random.normal(0, 1, num_samples),
        'target3': 0.4 * X['feature5'] + 0.3 * X['feature1'] + np.random.normal(0, 1, num_samples), 
        'target4': 0.9 * X['feature6'] + 0.3 * X['feature4'] + np.random.normal(0, 1, num_samples)
    })
    return X, Y

def perform_manova(X, Y):
    """
    Perform MANOVA test.

    Parameters:
    X (pd.DataFrame): Independent features.
    Y (pd.DataFrame): Dependent variables.

    Returns:
    results (MANOVA): MANOVA results.
    """
    data = pd.concat([X, Y], axis=1)
    formula = 'target1 + target2 + target3 + target4 ~ feature1 + feature2 + feature3 + feature4 + feature5 + feature6'
    manova = MANOVA.from_formula(formula, data=data)
    results = manova.mv_test()
    return results

def extract_p_values(results, X):
    """
    Extract p-values from MANOVA results.

    Parameters:
    results (MANOVA): MANOVA results.
    X (pd.DataFrame): Independent features.

    Returns:
    p_values (dict): p-values for each feature.
    """
    all_features = X.columns.tolist()
    p_values = {feature: results.results[feature]['stat']['Pr > F'][0] for feature in all_features}
    return p_values

def select_significant_features(p_values, alpha=0.05):
    """
    Select significant features based on p-values.

    Parameters:
    p_values (dict): p-values for each feature.
    alpha (float): Significance level (default=0.05).

    Returns:
    selected_features (list): Significant features.
    """
    selected_features = [feature for feature, p in p_values.items() if p < alpha]
    return selected_features

def main():
    num_samples = 150
    X, Y = generate_data(num_samples)
    results = perform_manova(X, Y)
    print("\nMANOVA Results:\n", results)
    p_values = extract_p_values(results, X)
    selected_features = select_significant_features(p_values)
    print("\nSelected Features Based on MANOVA (p < 0.05):", selected_features)

if __name__ == "__main__":
    main()