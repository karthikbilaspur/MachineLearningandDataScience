# advanced_eda.py

"""
Advanced Exploratory Data Analysis (EDA) techniques.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap

def calculate_descriptive_statistics(df):
    """
    Calculate descriptive statistics for the dataset.
    
    Parameters:
    df (pd.DataFrame): The dataset to analyze.
    """
    print("Mean:", df.mean())
    print("Median:", df.median())
    print("Mode:", df.mode())
    print("Standard Deviation:", df.std())
    print("Interquartile Range (IQR):", df.quantile(0.75) - df.quantile(0.25))
    print("Skewness:", df.skew())
    print("Kurtosis:", df.kurt())

def visualize_distributions(df):
    """
    Visualize distributions of the dataset.
    
    Parameters:
    df (pd.DataFrame): The dataset to visualize.
    """
    # Bar plot
    plt.figure(figsize=(8, 6))
    sns.countplot(x='category', data=df)
    plt.title('Bar Plot')
    plt.show()

    # Stacked bar graph
    plt.figure(figsize=(8, 6))
    sns.countplot(x='category', hue='subcategory', data=df)
    plt.title('Stacked Bar Graph')
    plt.show()

    # Histogram
    plt.figure(figsize=(8, 6))
    sns.histplot(df['value'], kde=True)
    plt.title('Histogram')
    plt.show()

    # Box plot
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='category', y='value', data=df)
    plt.title('Box Plot')
    plt.show()

    # Violin plot
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='category', y='value', data=df)
    plt.title('Violin Plot')
    plt.show()

def identify_outliers(df):
    """
    Identify outliers in the dataset.
    
    Parameters:
    df (pd.DataFrame): The dataset to analyze.
    """
    # Z-scores
    from scipy import stats
    z_scores = np.abs(stats.zscore(df['value']))
    print("Z-scores:", z_scores)

    # Isolation Forest
    from sklearn.ensemble import IsolationForest
    iso_forest = IsolationForest(contamination=0.1)
    outliers = iso_forest.fit_predict(df[['value']])
    print("Outliers:", outliers)

def perform_dimensionality_reduction(df):
    """
    Perform dimensionality reduction on the dataset.
    
    Parameters:
    df (pd.DataFrame): The dataset to reduce.
    """
    # PCA
    pca = PCA(n_components=2)
    reduced_df = pca.fit_transform(df)
    print("Reduced DataFrame (PCA):", reduced_df)

    # t-SNE
    tsne = TSNE(n_components=2)
    reduced_df_tsne = tsne.fit_transform(df)
    print("Reduced DataFrame (t-SNE):", reduced_df_tsne)

    # UMAP
    umap_model = umap.UMAP(n_components=2)
    reduced_df_umap = umap_model.fit_transform(df)
    print("Reduced DataFrame (UMAP):", reduced_df_umap)

if __name__ == "__main__":
    # Load the dataset
    df = pd.read_csv("data.csv")

    # Calculate descriptive statistics
    calculate_descriptive_statistics(df)

    # Visualize distributions
    visualize_distributions(df)

    # Identify outliers
    identify_outliers(df)

    # Perform dimensionality reduction
    perform_dimensionality_reduction(df)