import pandas as pd

# Load the dataset
data = pd.read_csv('main_data.csv')  # Update the path to your dataset

# Fill missing values with 0 for simplicity. This is a simplification and might not reflect the best approach for all analyses.
data_filled = data.fillna({
    'StringencyIndex_Average': 0,
    'PopulationVaccinated': 0,
    'ConfirmedCases': 0,
    'ConfirmedDeaths': 0
})

# Calculate correlation matrix among the relevant columns
correlation_matrix = data_filled[['StringencyIndex_Average', 'PopulationVaccinated', 'ConfirmedCases', 'ConfirmedDeaths']].corr()

print(correlation_matrix)
