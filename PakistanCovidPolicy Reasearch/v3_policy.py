import pandas as pd

# Load the dataset
file_path = 'main_data.csv'
data = pd.read_csv(file_path)

# Convert 'Date' to datetime format assuming YYYYMMDD
data['Date'] = pd.to_datetime(data['Date'], format='%Y%m%d')

# Sort by date to ensure chronological order
data.sort_values('Date', inplace=True)

# Keep only the relevant columns
data = data[['Date', 'V2B_Vaccine age eligibility/availability age floor (general population summary)', 'V2C_Vaccine age eligibility/availability age floor (at risk summary)']]

# Initialize columns to track changes
data['V2B_Changed'] = data['V2B_Vaccine age eligibility/availability age floor (general population summary)'].ne(data['V2B_Vaccine age eligibility/availability age floor (general population summary)'].shift())
data['V2C_Changed'] = data['V2C_Vaccine age eligibility/availability age floor (at risk summary)'].ne(data['V2C_Vaccine age eligibility/availability age floor (at risk summary)'].shift())

# Filter rows where either variable changes
changes = data[data['V2B_Changed'] | data['V2C_Changed']]

# Drop the change tracking columns as they are no longer needed for output
changes = changes.drop(columns=['V2B_Changed', 'V2C_Changed'])

# Extract month and year for each change
changes['Month'] = changes['Date'].dt.month_name()
changes['Year'] = changes['Date'].dt.year

# Select relevant columns for the output
changes = changes[['Month', 'Year', 'V2B_Vaccine age eligibility/availability age floor (general population summary)', 'V2C_Vaccine age eligibility/availability age floor (at risk summary)']]

# Print the changes directly to the terminal
print("Changes in vaccine age eligibility:")
print(changes.to_string(index=False))
