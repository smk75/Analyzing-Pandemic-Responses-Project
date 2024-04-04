import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('main_data.csv')

# Convert 'Date' column to datetime format and ensure it's the index of the DataFrame
data['Date'] = pd.to_datetime(data['Date'], format='%Y%m%d')
data.set_index('Date', inplace=True)
data.sort_index(inplace=True)

# Select the outcome variable and drop missing values
outcome = 'ConfirmedCases'
ts = data[outcome].dropna()

# Check if the time series is stationary
adf_test = adfuller(ts)
print('ADF Statistic: %f' % adf_test[0])
print('p-value: %f' % adf_test[1])

# Fit an ARIMA model (order (p,d,q) needs to be determined)
# Here I'm using (1,1,1) which is a common starting point, but should be tailored to your data
model = ARIMA(ts, order=(5,1,0))
model_fit = model.fit()

# Summary of the model
print(model_fit.summary())

# Plot the original series and the forecasted series
plt.figure(figsize=(10,6))
plt.plot(ts, label='Original')
plt.plot(model_fit.predict(), label='Forecast', alpha=0.7)
plt.title('ARIMA Model Forecast')
plt.xlabel('Date')
plt.ylabel(outcome)
plt.legend()
plt.show()
