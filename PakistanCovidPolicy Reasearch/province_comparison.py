import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'combined_daily_reports.xlsx'
data = pd.read_excel(file_path)

# Convert 'Report Date' to datetime format and sort data by it
data['Report Date'] = pd.to_datetime(data['Report Date'])
data.sort_values('Report Date', inplace=True)

# Aggregate data by 'Report Date' for overall trend analysis
daily_totals = data.groupby('Report Date').sum()

# Plotting daily trends for confirmed cases, deaths, and recoveries
plt.figure(figsize=(14, 6))

plt.subplot(1, 3, 1)
plt.plot(daily_totals.index, daily_totals['Confirmed'], label='Confirmed', color='blue')
plt.title('Daily Confirmed Cases')
plt.xticks(rotation=45)

plt.subplot(1, 3, 2)
plt.plot(daily_totals.index, daily_totals['Deaths'], label='Deaths', color='red')
plt.title('Daily Deaths')
plt.xticks(rotation=45)

plt.subplot(1, 3, 3)
plt.plot(daily_totals.index, daily_totals['Recovered'], label='Recovered', color='green')
plt.title('Daily Recovered Cases')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Grouping data by 'Province_State' for province-level analysis
province_totals = data.groupby('Province_State').sum()

# Taking top 10 provinces by total confirmed cases
top_provinces = province_totals.nlargest(10, 'Confirmed')

# Plotting top 10 provinces by confirmed cases, deaths, and recoveries
plt.figure(figsize=(14, 18))

plt.subplot(3, 1, 1)
sns.barplot(x=top_provinces['Confirmed'], y=top_provinces.index)
plt.title('Top 10 Provinces by Confirmed Cases')
plt.xlabel('Total Confirmed Cases')
plt.ylabel('Province/State')

plt.subplot(3, 1, 2)
sns.barplot(x=top_provinces['Deaths'], y=top_provinces.index, color='red')
plt.title('Top 10 Provinces by Deaths')
plt.xlabel('Total Deaths')
plt.ylabel('Province/State')

plt.subplot(3, 1, 3)
sns.barplot(x=top_provinces['Recovered'], y=top_provinces.index, color='green')
plt.title('Top 10 Provinces by Recovered Cases')
plt.xlabel('Total Recovered Cases')
plt.ylabel('Province/State')

plt.tight_layout()
plt.show()
