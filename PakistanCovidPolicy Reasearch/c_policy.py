import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('main_data.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')

df['YearMonth'] = df['Date'].dt.to_period('M')

# Aggregating policy levels by maximum level enacted each month
# Assuming each row represents a day, and policies can vary within the month
monthly_policies = df.groupby('YearMonth').agg({
    'C1M_School closing': 'max',
    'C2M_Workplace closing': 'max',
    'C3M_Cancel public events': 'max',
    'C4M_Restrictions on gatherings': 'max',
    'C5M_Close public transport': 'max',
    'C6M_Stay at home requirements': 'max',
    'C7M_Restrictions on internal movement': 'max',
    'C8EV_International travel controls': 'max',
}).reset_index()

# Renaming the policies for better understanding
policy_names = {
    'C1M_School closing': 'School Closing',
    'C2M_Workplace closing': 'Workplace Closing',
    'C3M_Cancel public events': 'Cancel Public Events',
    'C4M_Restrictions on gatherings': 'Restrictions on Gatherings',
    'C5M_Close public transport': 'Close Public Transport',
    'C6M_Stay at home requirements': 'Stay at Home Requirements',
    'C7M_Restrictions on internal movement': 'Restrictions on Internal Movement',
    'C8EV_International travel controls': 'International Travel Controls',
}

monthly_policies.rename(columns=policy_names, inplace=True)

# Converting YearMonth back to string for plotting
monthly_policies['YearMonth'] = monthly_policies['YearMonth'].astype(str)

# Setting the YearMonth as index
monthly_policies.set_index('YearMonth', inplace=True)

# Plotting the heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(monthly_policies.T, cmap='viridis', annot=True, fmt=".1f", linewidths=.5)

plt.title('Heatmap of Containment and Closure Policy Intensities Over Time in Pakistan')
plt.xlabel('Date (Year-Month)')
plt.ylabel('Policy')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()