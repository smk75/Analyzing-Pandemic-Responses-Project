import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('main_data.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')

# Extract year and month from the 'Date' column for grouping
df['YearMonth'] = df['Date'].dt.to_period('M')

# Aggregate the vaccination policy levels by maximum level enacted each month
vaccination_policies = df.groupby('YearMonth').agg({
    'V1_Vaccine Prioritisation (summary)': 'max',  # Placeholder for the actual variable name
    'V2A_Vaccine Availability (summary)': 'max',  # Placeholder for the actual variable name
}).reset_index()

# Renaming the policies for better understanding
vaccination_policy_names = {
    'V1_Vaccine Prioritisation (summary)': 'Vaccine Prioritisation',
    'V2A_Vaccine Availability (summary)': 'Vaccine Eligibility/Availability',
}

vaccination_policies.rename(columns=vaccination_policy_names, inplace=True)

# Converting YearMonth to string for plotting
vaccination_policies['YearMonth'] = vaccination_policies['YearMonth'].astype(str)

# Setting YearMonth as index
vaccination_policies.set_index('YearMonth', inplace=True)

# Plotting the heatmap for Vaccination Policies
plt.figure(figsize=(12, 8))
sns.heatmap(vaccination_policies.T, cmap='viridis', annot=True, fmt=".1f", linewidths=.5)

plt.title('Heatmap of Vaccination Policy Intensities Over Time in Pakistan')
plt.xlabel('Date (Year-Month)')
plt.ylabel('Policy')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
