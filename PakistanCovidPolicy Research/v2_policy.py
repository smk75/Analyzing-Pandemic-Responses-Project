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
# Replace 'V1..summary.', 'V2..summary.', etc., with the actual column names from your dataset
vaccination_policies = df.groupby('YearMonth').agg({
    'V1_Vaccine Prioritisation (summary)': 'max', 
    'V2A_Vaccine Availability (summary)': 'max',
    'V2D_Medically/ clinically vulnerable (Non-elderly)': 'max',
    'V2E_Education': 'max',
    'V2F_Frontline workers  (non healthcare)': 'max',
    'V2G_Frontline workers  (healthcare)': 'max',
}).reset_index()

# Renaming the policies for better understanding
vaccination_policy_names = {
    'V1_Vaccine Prioritisation (summary)': 'Vaccine Prioritisation',
    'V2A_Vaccine Availability (summary)': 'Vaccine Eligibility/Availability',
    'V2D_Medically/ clinically vulnerable (Non-elderly)': 'Number of vulnerable',
    'V2E_Education': 'Vaccine Education',
    'V2F_Frontline workers (non-healthcare)': 'Non-healthcare frontline workers',
    'V2G_Frontline workers (healthcare)': 'healthcare frontline workers',
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
