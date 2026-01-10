# Advanced Time Series Analysis

"""
Handling Missing Values and Outliers
------------------------------------

Missing values and outliers can significantly impact time series analysis and forecasting.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("stock_data.csv", parse_dates=True, index_col="Date")

# Handling Missing Values
# ------------------------

# Forward Fill
df_ffill = df.fillna(method='ffill')

# Backward Fill
df_bfill = df.fillna(method='bfill')

# Interpolation
df_interpolate = df.interpolate(method='linear')

# Outlier Detection
# -----------------

# Z-Score Method
from scipy import stats
z_scores = np.abs(stats.zscore(df))
outliers = df[z_scores > 3]

# Rolling Window Method
window_size = 10
rolling_mean = df.rolling(window_size).mean()
rolling_std = df.rolling(window_size).std()
outliers_rw = df[(df > rolling_mean + 3 * rolling_std) | (df < rolling_mean - 3 * rolling_std)]

"""
Transformations for Stability
-----------------------------

Transformations can help stabilize variance and make time series data more manageable.
"""

# Log Transformation
df_log = np.log(df)

# Box-Cox Transformation
from scipy import stats
df_boxcox, lambda_ = stats.boxcox(df)

# Scaling (Standardization/Min-Max)
from sklearn.preprocessing import StandardScaler, MinMaxScaler
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

"""
Lag Features and Rolling Statistics
------------------------------------

Lag features and rolling statistics help capture temporal dependencies.
"""

# Lag Features
df_lag = df.shift(1)

# Rolling Mean and Rolling Standard Deviation
window_size = 10
df_rolling_mean = df.rolling(window_size).mean()
df_rolling_std = df.rolling(window_size).std()

"""
Advanced Statistical Tests
---------------------------

Advanced statistical tests verify assumptions and ensure data and models behave as expected.
"""

# KPSS Test
from statsmodels.tsa.stattools import kpss
kpss_stat, p_value, _, _ = kpss(df)

# Ljung-Box Test
from statsmodels.stats.diagnostic import acorr_ljungbox
ljung_box_stat, p_value = acorr_ljungbox(df, lags=10)

"""
Forecasting Models and Machine Learning for Time Series
------------------------------------------------------

Time series forecasting can be approached using classical statistical models and machine learning techniques.
"""

# ARIMA Model
from statsmodels.tsa.arima.model import ARIMA
model = ARIMA(df, order=(1,1,1))
model_fit = model.fit()

# SARIMA Model
from statsmodels.tsa.statespace.sarimax import SARIMAX
model = SARIMAX(df, order=(1,1,1), seasonal_order=(1,1,1,12))
model_fit = model.fit()

# Exponential Smoothing (Holt-Winters)
from statsmodels.tsa.holtwinters import ExponentialSmoothing
model = ExponentialSmoothing(df, trend='add', seasonal='add', seasonal_periods=12)
model_fit = model.fit()

# Random Forests
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=100)
model.fit(df_lag, df)

# LSTMs and GRUs (Deep Learning)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
model = Sequential()
model.add(LSTM(50, input_shape=(1, 1)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(df_lag, df, epochs=100, batch_size=32)