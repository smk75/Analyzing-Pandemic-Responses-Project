import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Load the dataset
data = pd.read_csv('main_data.csv')  # Update the path to your dataset

# Convert 'Date' column to datetime format and ensure it's the index of the DataFrame
data['Date'] = pd.to_datetime(data['Date'], format='%Y%m%d')
data.set_index('Date', inplace=True)
data.sort_index(inplace=True)

# List the columns you believe could have made a major impact on the number of confirmed cases
intervention_columns = [
    'C6M_Stay at home requirements',  # Assuming this is the stay at home requirement
    'C4M_Restrictions on gatherings',  # Assuming this is for public events restriction
    'C5M_Close public transport',  # Assuming this is for public transport restriction
    'E1_Income support',  # Assuming this is for income support
    'H6M_Facial Coverings',  # Assuming this is for facial coverings
    'V3_Vaccine Financial Support (summary)',  # Assuming this is for vaccine financial support
    'V4_Mandatory Vaccination (summary)',   # Assuming this is when the vaccine became mandatory
    'C2M_Workplace closing',
    'C3M_Cancel public events',
    'C7M_Restrictions on internal movement',
    'H2_Testing policy',
    'H3_Contact tracing',
    'H7_Vaccination policy',
    'H8M_Protection of elderly people',
    'PopulationVaccinated',
    'StringencyIndex_Average',
    'GovernmentResponseIndex_Average',
    'ContainmentHealthIndex_Average',
    'EconomicSupportIndex',
    








]

# Verify the correct names of the columns by inspecting the data
print(data.columns)

# Fit the ARIMAX model using the intervention columns as exogenous variables
# Make sure the exogenous variables are binary flags indicating the presence of the intervention
exog_data = data[intervention_columns].fillna(0)  # Replace NaN with 0 if necessary

# Select the outcome variable, assuming 'ConfirmedCases' is the correct column name
outcome = 'ConfirmedCases'
ts = data[outcome].dropna()

# Fit the ARIMAX model using the intervention columns as exogenous variables
# The order (5,1,0) is chosen based on the best fit from auto_arima
model_arimax = SARIMAX(ts, order=(5,1,0), exog=exog_data)
model_arimax_fit = model_arimax.fit()

# Summary of the ARIMAX model
arimax_summary = model_arimax_fit.summary()
print(arimax_summary)
