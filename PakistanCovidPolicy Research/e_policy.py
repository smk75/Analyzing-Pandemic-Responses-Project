
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('main_data.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')

# Assuming the corrected column names are as follows (please replace with the actual column names):
economic_policy_columns = {
    'E1_Income support': 'Income Support',
    'E2_Debt/contract relief': 'Debt/Contract Relief',
    # 'E3_Fiscal measures' and 'E4_International support' might require preprocessing due to their monetary nature
}

# Filter the DataFrame for the relevant columns (including Date for grouping)
df_economic = df[['Date'] + list(economic_policy_columns.keys())]

# Convert the 'Date' column to datetime format for easier manipulation
df_economic['Date'] = pd.to_datetime(df_economic['Date'], format='%Y%m%d')

# Extract year and month from the 'Date' column for grouping
df_economic['YearMonth'] = df_economic['Date'].dt.to_period('M')

# Aggregating economic policy levels by maximum level enacted each month
economic_policies = df_economic.groupby('YearMonth').agg({
    'E1_Income support': 'max',  # Placeholder for Income support
    'E2_Debt/contract relief': 'max',  # Placeholder for Debt/contract relief
}).reset_index()

# Renaming the policies for better understanding
economic_policies.rename(columns=economic_policy_columns, inplace=True)

# Converting YearMonth back to string for plotting
economic_policies['YearMonth'] = economic_policies['YearMonth'].astype(str)

# Setting the YearMonth as index
economic_policies.set_index('YearMonth', inplace=True)

# Plotting the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(economic_policies.T, cmap='viridis', annot=True, fmt=".1f", linewidths=.5)

plt.title('Heatmap of Economic Policy Intensities Over Time in Pakistan')
plt.xlabel('Date (Year-Month)')
plt.ylabel('Policy')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()