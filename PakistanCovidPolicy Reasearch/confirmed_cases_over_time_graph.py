import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('main_data.csv')

# Convert the 'Date' column to datetime format for easier analysis
df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')

# Plotting the trend of confirmed COVID-19 cases over time
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['ConfirmedCases'], label='Confirmed Cases', color='blue')
plt.title('Trend of Confirmed COVID-19 Cases in Pakistan')
plt.xlabel('Date')
plt.ylabel('Number of Confirmed Cases')
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
plt.legend()  # Add a legend to the plot
plt.tight_layout()  # Adjust layout to not cut off labels
plt.show()  # Display the plot
