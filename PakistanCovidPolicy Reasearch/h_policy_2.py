import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming the file has been re-uploaded and is accessible at the specified path
df = pd.read_csv('main_data.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')

# Extract year and month from the 'Date' column for grouping
df['YearMonth'] = df['Date'].dt.to_period('M')

# Assuming correct column names for Health System Policies. Replace placeholders as necessary.
health_policy_columns = {
    'H4_Emergency investment in healthcare': 'max',  
    'H5_Investment in vaccines': 'max',
}

# Aggregating health system policy levels by maximum level enacted each month
health_policies = df.groupby('YearMonth').agg(health_policy_columns).reset_index()

# Renaming columns for better understanding, if needed
health_policy_names = {
    'H4_Emergency investment in healthcare': 'Emergency Investment in healthcare',  
    'H5_Investment in vaccines': 'Investment in vaccines',
}

health_policies.rename(columns=health_policy_names, inplace=True)

# Converting YearMonth to string for plotting
health_policies['YearMonth'] = health_policies['YearMonth'].astype(str)

# Setting YearMonth as index
health_policies.set_index('YearMonth', inplace=True)

# Plotting the heatmap for Health System Policies
plt.figure(figsize=(12, 8))
sns.heatmap(health_policies.T, cmap='viridis', annot=True, fmt=".1f", linewidths=.5)

plt.title('Heatmap of Health System Policy Intensities Over Time in Pakistan')
plt.xlabel('Date (Year-Month)')
plt.ylabel('Policy')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
