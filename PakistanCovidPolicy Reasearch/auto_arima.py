# You might need to install the pmdarima package first. Uncomment the next line if you haven't installed pmdarima yet.
# !pip install pmdarima

import pandas as pd
from pmdarima import auto_arima
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('main_data.csv')  # Update the path to your dataset

# Convert 'Date' column to datetime format and ensure it's the index of the DataFrame
data['Date'] = pd.to_datetime(data['Date'], format='%Y%m%d')
data.set_index('Date', inplace=True)
data.sort_index(inplace=True)

# Select the outcome variable and drop missing values
outcome = 'ConfirmedCases'
ts = data[outcome].dropna()  # Define the time series

# Fit the ARIMA model using auto_arima
auto_model = auto_arima(ts, start_p=0, start_q=0,
                        test='adf',       # use adf test to find optimal 'd'
                        max_p=5, max_q=5, # maximum p and q
                        m=1,              # frequency of series (non-seasonal data)
                        d=None,           # let model determine 'd'
                        seasonal=False,   # No Seasonality
                        stepwise=True,    # Use stepwise algorithm
                        suppress_warnings=True,
                        error_action='ignore',
                        trace=True)

# Summary of the model
print(auto_model.summary())

# Forecast using the best ARIMA model
forecast, conf_int = auto_model.predict(n_periods=30, return_conf_int=True)  # Forecast next 30 periods

# Plot the original series and the forecasted series
plt.figure(figsize=(10, 6))
plt.plot(ts.index, ts, label='Observed', alpha=0.6)
forecast_index = pd.date_range(ts.index[-1], periods=31, closed='right')  # Generate future dates for forecasting
plt.plot(forecast_index, forecast, label='Forecast', alpha=0.7)
plt.fill_between(forecast_index, conf_int[:, 0], conf_int[:, 1], alpha=0.3, label='Confidence Interval')
plt.axvline(ts.index[-1], color='gray', linestyle='--', label='Last Observed Data Point')
plt.title('ARIMA Forecast')
plt.xlabel('Date')
plt.ylabel(outcome)
plt.legend()
plt.show()
