# exploratory_data_analysis.py

"""
Exploratory Data Analysis (EDA) is a important step in data analysis 
which focuses on understanding patterns, trends and relationships through 
statistical tools and visualizations.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr
wr.filterwarnings('ignore')

def load_dataset(file_path):
    """
    Load the dataset from a CSV file.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded dataset.
    """
    return pd.read_csv(file_path)

def analyze_data(df):
    """
    Analyze the dataset.
    
    Parameters:
    df (pd.DataFrame): The dataset to analyze.
    """
    print("Shape of the dataset:", df.shape)
    print("Info of the dataset:")
    print(df.info())
    print("Describe of the dataset:")
    print(df.describe().T)
    print("Columns of the dataset:")
    print(df.columns.tolist())

def check_missing_values(df):
    """
    Check for missing values in the dataset.
    
    Parameters:
    df (pd.DataFrame): The dataset to check.
    """
    print("Missing values in each column:")
    print(df.isnull().sum())

def check_duplicate_values(df):
    """
    Check for duplicate values in the dataset.
    
    Parameters:
    df (pd.DataFrame): The dataset to check.
    """
    print("Unique values in each column:")
    print(df.nunique())

def univariate_analysis(df):
    """
    Perform univariate analysis on the dataset.
    
    Parameters:
    df (pd.DataFrame): The dataset to analyze.
    """
    # Bar plot for evaluating the count of the wine with its quality rate
    quality_counts = df['quality'].value_counts()
    plt.figure(figsize=(8, 6))
    plt.bar(quality_counts.index, quality_counts, color='deeppink')
    plt.title('Count Plot of Quality')
    plt.xlabel('Quality')
    plt.ylabel('Count')
    plt.show()

    # Kernel density plot for understanding variance in the dataset
    sns.set_style("darkgrid")
    numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns
    plt.figure(figsize=(14, len(numerical_columns) * 3))
    for idx, feature in enumerate(numerical_columns, 1):
        plt.subplot(len(numerical_columns), 2, idx)
        sns.histplot(df[feature], kde=True)
        plt.title(f"{feature} | Skewness: {round(df[feature].skew(), 2)}")
    plt.tight_layout()
    plt.show()

    # Swarm plot for showing the outlier in the data
    plt.figure(figsize=(10, 8))
    sns.swarmplot(x="quality", y="alcohol", data=df, palette='viridis')
    plt.title('Swarm Plot for Quality and Alcohol')
    plt.xlabel('Quality')
    plt.ylabel('Alcohol')
    plt.show()

def bivariate_analysis(df):
    """
    Perform bivariate analysis on the dataset.
    
    Parameters:
    df (pd.DataFrame): The dataset to analyze.
    """
    # Pair plot for showing the distribution of the individual variables
    sns.set_palette("Pastel1")
    plt.figure(figsize=(10, 6))
    sns.pairplot(df)
    plt.suptitle('Pair Plot for DataFrame')
    plt.show()

    # Violin plot for examining the relationship between alcohol and Quality
    df['quality'] = df['quality'].astype(str)
    plt.figure(figsize=(10, 8))
    sns.violinplot(x="quality", y="alcohol", data=df, palette={
                   '3': 'lightcoral', '4': 'lightblue', '5': 'lightgreen', '6': 'gold', '7': 'lightskyblue', '8': 'lightpink'}, alpha=0.7)
    plt.title('Violin Plot for Quality and Alcohol')
    plt.xlabel('Quality')
    plt.ylabel('Alcohol')
    plt.show()

    # Box plot for examining the relationship between alcohol and Quality
    sns.boxplot(x='quality', y='alcohol', data=df)

def multivariate_analysis(df):
    """
    Perform multivariate analysis on the dataset.
    
    Parameters:
    df (pd.DataFrame): The dataset to analyze.
    """
    # Correlation matrix plot
    plt.figure(figsize=(15, 10))
    sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='Pastel2', linewidths=2)
    plt.title('Correlation Heatmap')
    plt.show()

if __name__ == "__main__":
    # Load the dataset
    df = load_dataset("/content/WineQT.csv")

    # Analyze the dataset
    analyze_data(df)

    # Check for missing values
    check_missing_values(df)

    # Check for duplicate values
    check_duplicate_values(df)

    # Perform univariate analysis
    univariate_analysis(df)

    # Perform bivariate analysis
    bivariate_analysis(df)

    # Perform multivariate analysis
    multivariate_analysis(df)