import pandas as pd
import folium
from folium.plugins import HeatMap

# Load the data
file_path = 'combined_daily_reports.xlsx'
data = pd.read_excel(file_path)

# Ensure the data types are correct; sometimes lat/long comes as strings
data['Lat'] = pd.to_numeric(data['Lat'], errors='coerce')
data['Long_'] = pd.to_numeric(data['Long_'], errors='coerce')

# Drop any rows that have NaN values in 'Lat' or 'Long_' after conversion
data.dropna(subset=['Lat', 'Long_'], inplace=True)

# Initialize a Folium map at a central location
map = folium.Map(location=[30.3753, 69.3451], zoom_start=5)
folium.TileLayer(
    'Stamen Terrain',
    attr='Map data by OpenStreetMap, under ODbL'
).add_to(map)



# Prepare data for the HeatMap; adjust 'Confirmed' if using a different value column
heat_data = [[row['Lat'], row['Long_'], row['Confirmed']] for index, row in data.iterrows()]

# Create and add a HeatMap layer
HeatMap(heat_data).add_to(map)

# Save the map to an HTML file
map.save('pakistan_heatmap.html')
