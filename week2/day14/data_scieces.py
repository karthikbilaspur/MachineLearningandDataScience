# data_science_techniques.py

import numpy as np
import pandas as pd
from statsmodels.multivariate.manova import MANOVA
from scipy.stats import norm
import matplotlib.pyplot as plt

# MANOVA Test
def manova_test(data, dependent_vars, independent_var):
    """
    Perform MANOVA test.

    Parameters:
    data (pd.DataFrame): Dataframe containing dependent and independent variables
    dependent_vars (list): List of dependent variable names
    independent_var (str): Name of independent variable

    Returns:
    MANOVA: MANOVA test results
    """
    formula = ' + '.join(dependent_vars) + ' ~ ' + independent_var
    manova = MANOVA.from_formula(formula, data=data)
    return manova.mv_test()

# Bayesian Statistics
def bayesian_update(prior_mean, prior_std, likelihood_mean, likelihood_std, data):
    """
    Update prior distribution with likelihood and data.

    Parameters:
    prior_mean (float): Prior mean
    prior_std (float): Prior standard deviation
    likelihood_mean (float): Likelihood mean
    likelihood_std (float): Likelihood standard deviation
    data (np.ndarray): Data

    Returns:
    tuple: Posterior mean and standard deviation
    """
    posterior_mean = (prior_mean / prior_std**2 + data.sum() / likelihood_std**2) / (1 / prior_std**2 + len(data) / likelihood_std**2)
    posterior_std = np.sqrt(1 / (1 / prior_std**2 + len(data) / likelihood_std**2))
    return posterior_mean, posterior_std

# Matrices
def matrix_operations():
    # Create a matrix
    A = np.array([[1, 2], [3, 4]])

    # Perform matrix multiplication
    B = np.array([[5, 6], [7, 8]])
    C = np.dot(A, B)

    # Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)

    return A, B, C, eigenvalues, eigenvectors

def main():
    # MANOVA Test
    np.random.seed(0)
    data = pd.DataFrame({
        'Time_Spent': np.random.normal(10, 2, 100),
        'Pages_Visited': np.random.normal(5, 1, 100),
        'Region': np.random.choice(['A', 'B', 'C'], 100)
    })
    manova_results = manova_test(data, ['Time_Spent', 'Pages_Visited'], 'Region')
    print("MANOVA Results:")
    print(manova_results)

    # Bayesian Statistics
    prior_mean = 0
    prior_std = 1
    likelihood_mean = 0
    likelihood_std = 1
    data = np.random.normal(0, 1, 100)
    posterior_mean, posterior_std = bayesian_update(prior_mean, prior_std, likelihood_mean, likelihood_std, data)
    print("\nPosterior Mean:", posterior_mean)
    print("Posterior Standard Deviation:", posterior_std)

    # Matrices
    A, B, C, eigenvalues, eigenvectors = matrix_operations()
    print("\nMatrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
    print("\nMatrix C (A * B):")
    print(C)
    print("\nEigenvalues of A:")
    print(eigenvalues)
    print("\nEigenvectors of A:")
    print(eigenvectors)

if __name__ == "__main__":
    main()