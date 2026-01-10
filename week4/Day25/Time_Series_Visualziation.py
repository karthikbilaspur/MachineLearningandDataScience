# Time Series Analysis & Visualization in Python

"""
Time Series Analysis:
--------------------

Time series analysis is a statistical technique used to analyze and forecast data 
that is collected over time. It involves examining patterns, trends, and correlations 
in the data to understand the underlying mechanisms that drive the data.

Time Series Components:
----------------------

1. Trend: The overall direction or pattern in the data.
2. Seasonality: Regular fluctuations that occur at fixed intervals (e.g., daily, weekly, yearly).
3. Noise: Random, irregular variations in the data.

Time Series Visualization:
-------------------------

Visualization is a crucial step in time series analysis. It helps to:

1. Identify patterns and trends
2. Detect anomalies and outliers
3. Understand seasonality and correlations
4. Evaluate model performance

Python Libraries for Time Series Analysis:
-----------------------------------------

1. Pandas: Data manipulation and analysis
2. NumPy: Numerical computations
3. Matplotlib and Seaborn: Data visualization
4. Statsmodels: Statistical modeling and analysis
"""

# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller

# Load the dataset
df = pd.read_csv("stock_data.csv", parse_dates=True, index_col="Date")

"""
Data Preparation:
-----------------

1. Load the dataset
2. Convert the date column to datetime format
3. Set the date column as the index
"""

# Drop unnecessary columns
df.drop(columns='Unnamed: 0', inplace=True)

# Plot High Stock Prices
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x=df.index, y='High', label='High Price', color='blue')
plt.xlabel('Date')
plt.ylabel('High')
plt.title('Share Highest Price Over Time')
plt.show()

"""
Time Series Visualization:
-------------------------

1. Line plots: To visualize trends and patterns
2. Autocorrelation plots: To detect seasonality and correlations
"""

# Resampling Data
df_resampled = df.resample('ME').mean(numeric_only=True)
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_resampled, x=df_resampled.index, y='High', label='Month Wise Average High Price', color='blue')
plt.xlabel('Date (Monthly)')
plt.ylabel('High')
plt.title('Monthly Resampling Highest Price Over Time')
plt.show()

# Detecting Seasonality with Autocorrelation
if 'Date' not in df.columns:
    print("'Date' is already the index or not present in the DataFrame.")
else:
    df.set_index('Date', inplace=True)
plt.figure(figsize=(12, 6))
plot_acf(df['High'], lags=40)
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Function (ACF) Plot')
plt.show()

"""
Stationarity Test:
------------------

1. Augmented Dickey-Fuller (ADF) test: To check if the time series is stationary
"""

# Testing Stationarity with ADF test
result = adfuller(df['High'])
print('ADF Statistic:', result[0])
print('p-value:', result[1])
print('Critical Values:', result[4])

# Differencing to Achieve Stationarity
df['high_diff'] = df['High'].diff()
plt.figure(figsize=(12, 6))
plt.plot(df['High'], label='Original High', color='blue')
plt.plot(df['high_diff'], label='Differenced High', linestyle='--', color='green')
plt.legend()
plt.title('Original vs Differenced High')
plt.show()

# Smoothing Data with Moving Average
window_size = 120
df['high_smoothed'] = df['High'].rolling(window=window_size).mean()
plt.figure(figsize=(12, 6))
plt.plot(df['High'], label='Original High', color='blue')
plt.plot(df['high_smoothed'], label=f'Moving Average (Window={window_size})', linestyle='--', color='orange')
plt.xlabel('Date')
plt.ylabel('High')
plt.title('Original vs Moving Average')
plt.legend()
plt.show()

# Original Data Vs Differenced Data
df_combined = pd.concat([df['High'], df['high_diff']], axis=1)
print(df_combined.head())

# Drop NaN values
df.dropna(subset=['high_diff'], inplace=True)

# ADF test after differencing
result = adfuller(df['high_diff'])
print('ADF Statistic:', result[0])
print('p-value:', result[1])
print('Critical Values:', result[4])