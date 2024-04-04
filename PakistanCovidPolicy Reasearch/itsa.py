import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Load the dataset
data = pd.read_csv('main_data.csv')  # Update the path to your dataset

# Convert 'Date' column to datetime format and sort the data
data['Date'] = pd.to_datetime(data['Date'], format='%Y%m%d')
data.sort_values('Date', inplace=True)

# Define your intervention date here
intervention_date = pd.to_datetime('2022-02-01')  # Replace with your actual intervention date

# Create the necessary variables for ITSA
data['Time'] = np.arange(len(data))
data['Intervention'] = (data['Date'] >= intervention_date).astype(int)
data['TimeAfterIntervention'] = data['Time'] - data.loc[data['Intervention'] == 1, 'Time'].min()
data['TimeAfterIntervention'] = data['TimeAfterIntervention'] * data['Intervention']

# Specify the outcome variable you're interested in
outcome = 'ConfirmedCases'  # Replace with your outcome variable

# Fit the segmented regression model
model_formula = f'{outcome} ~ Time + Intervention + TimeAfterIntervention'
itsa_model = ols(model_formula, data=data).fit()

# Print the model summary to see the results
print(itsa_model.summary())

# Check for model assumptions
fig = plt.figure(figsize=(15, 8))
sm.graphics.plot_regress_exog(itsa_model, 'Intervention', fig=fig)

# Plot the observed and fitted values to visualize the intervention's effect
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data[outcome], label='Observed', alpha=0.6)
plt.plot(data['Date'], itsa_model.fittedvalues, label='Fitted', color='red')
plt.axvline(x=intervention_date, color='gray', linestyle='--', label='Intervention')

# Plotting the confidence intervals
predictions = itsa_model.get_prediction().summary_frame(alpha=0.05)
plt.fill_between(data['Date'], predictions['obs_ci_lower'], predictions['obs_ci_upper'], color='red', alpha=0.3, label='95% Confidence Interval')

plt.legend()
plt.xlabel('Date')
plt.ylabel(outcome)
plt.title(f'Interrupted Time Series Analysis of {outcome}')
plt.show()
