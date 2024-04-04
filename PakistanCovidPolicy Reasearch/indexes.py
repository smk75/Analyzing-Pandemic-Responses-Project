import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('data.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')

#df_filtered = df[(df['Date'] >= '2022-02-01') & (df['Date'] <= '2022-03-31')]

# Extract year and month from the 'Date' column for grouping
#df_filtered['YearMonth'] = df_filtered['Date'].dt.to_period('M')
df['YearMonth'] = df['Date'].dt.to_period('M')

# Aggregate the given numeric variables by calculating their average each month
numeric_variables = df.groupby('YearMonth').agg({
    'PopulationVaccinated': 'mean',  # Average of PopulationVaccinated per month
    'StringencyIndex_Average': 'mean',  # Average of StringencyIndex_Average per month
    'GovernmentResponseIndex_Average': 'mean',  # Average of GovernmentResponseIndex_Average per month
    'ContainmentHealthIndex_Average': 'mean',  # Average of ContainmentHealthIndex_Average per month
    'EconomicSupportIndex': 'mean',  # Average of EconomicSupportIndex per month
}).reset_index()

# Renaming the variables for better understanding
numeric_variable_names = {
    'PopulationVaccinated': 'Population Vaccinated',
    'StringencyIndex_Average': 'Stringency Index',
    'GovernmentResponseIndex_Average': 'Government Response Index',
    'ContainmentHealthIndex_Average': 'Containment & Health Index',
    'EconomicSupportIndex': 'Economic Support Index',
}

numeric_variables.rename(columns=numeric_variable_names, inplace=True)

# Converting YearMonth to string for plotting
numeric_variables['YearMonth'] = numeric_variables['YearMonth'].astype(str)

# Setting YearMonth as index
numeric_variables.set_index('YearMonth', inplace=True)

# Plotting the heatmap for the numeric variables
plt.figure(figsize=(14, 10))  # Increase the figure size
sns.heatmap(numeric_variables.T, cmap='viridis', annot=True, fmt=".2f", linewidths=.5,
            annot_kws={"size": 6})  # Adjust annotation font size

plt.title('Heatmap of Numeric Variables Over Time in Pakistan', size=14)  # Adjust title font size
plt.xlabel('Date (Year-Month)', size=12)  # Adjust X-axis label font size
plt.ylabel('Variable', size=12)  # Adjust Y-axis label font size
plt.xticks(rotation=45, size=10)  # Rotate X-axis labels and adjust font size
plt.yticks(size=10)  # Adjust Y-axis labels font size

plt.tight_layout()
plt.show()
