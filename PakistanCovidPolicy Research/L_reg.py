from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd

# Load the dataset
data = pd.read_csv('main_data.csv')  # Update the path to your dataset

# Fill missing values with 0 for simplicity. This is a simplification and might not reflect the best approach for all analyses.
data_filled = data.fillna({
    'StringencyIndex_Average': 0,
    'ContainmentHealthIndex_Average': 0,
    'PopulationVaccinated': 0,
    'ConfirmedCases': 0
})

# Selecting predictors and the outcome for the model
X = data_filled[['StringencyIndex_Average', 'ContainmentHealthIndex_Average', 'PopulationVaccinated']]
y_cases = data_filled['ConfirmedCases']

# Splitting the data into training and testing sets
X_train, X_test, y_cases_train, y_cases_test = train_test_split(X, y_cases, test_size=0.2, random_state=42)

# Initializing and fitting the linear regression model
model_cases = LinearRegression()
model_cases.fit(X_train, y_cases_train)

# Predicting on the test set
y_cases_pred = model_cases.predict(X_test)

# Calculating the Root Mean Squared Error (RMSE) for the model
rmse_cases = np.sqrt(mean_squared_error(y_cases_test, y_cases_pred))

# Extracting model coefficients
coefficients_cases = model_cases.coef_

# Printing the RMSE and model coefficients
print(f'RMSE for ConfirmedCases model: {rmse_cases}')
print(f'Model Coefficients: {coefficients_cases}')
