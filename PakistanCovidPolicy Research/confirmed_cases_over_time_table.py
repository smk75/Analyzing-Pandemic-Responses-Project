import pandas as pd

# Load the dataset
df = pd.read_csv('data.csv')  # Replace with the path to your dataset

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')

# Extract year and month from the 'Date' column
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Group by year and month, then sum up the confirmed cases for each group
monthly_cumulative = df.groupby(['Year', 'Month'])['ConfirmedCases'].sum().reset_index()

# Calculate the month-over-month difference in confirmed cases to get the net increase/decrease
monthly_cumulative['MoM_Change'] = monthly_cumulative['ConfirmedCases'].diff()

# Adjust the first row's MoM_Change to NaN or 0 because there's no previous month data to compare with
monthly_cumulative['MoM_Change'].iloc[0] = None  # or 0 if you prefer to mark no change as 0

# Rename columns to match the requested format
monthly_cumulative.rename(columns={'ConfirmedCases': 'Confirmed Cases', 'MoM_Change': 'MoM Change in Cases'}, inplace=True)

# Display the table
#print(monthly_cumulative)

# Identify the rows with the maximum increase and the maximum decrease in MoM Change in Cases
max_increase_row = monthly_cumulative.loc[monthly_cumulative['MoM Change in Cases'].idxmax()]
max_decrease_row = monthly_cumulative.loc[monthly_cumulative['MoM Change in Cases'].idxmin()]

# Printing out the results
print(f"Month with the most increase in confirmed cases: {int(max_increase_row['Year'])}-{int(max_increase_row['Month'])}, Increase: {max_increase_row['MoM Change in Cases']}")
print(f"Month with the biggest decrease in confirmed cases: {int(max_decrease_row['Year'])}-{int(max_decrease_row['Month'])}, Decrease: {max_decrease_row['MoM Change in Cases']}")


"""

monthly_summary = df.groupby(['Year', 'Month'])['ConfirmedCases'].sum().reset_index()
# Rename columns to match the requested format
monthly_summary.rename(columns={'ConfirmedCases': 'Confirmed Cases'}, inplace=True)

# Display the table
print(monthly_summary)
"""

