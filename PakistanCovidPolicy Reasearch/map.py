import pandas as pd
import folium

def plot_province_data_on_map(excel_path):
    # Load the data from the Excel file
    data = pd.read_excel(excel_path)

    # Create a map centered around the approximate center of Pakistan
    pakistan_map = folium.Map(location=[30.3753, 69.3451], zoom_start=5)

    # Iterate through the dataframe and add each province as a marker on the map
    for index, row in data.iterrows():
        # Skip rows where latitude or longitude is missing
        if pd.isna(row['Lat']) or pd.isna(row['Long_']):
            continue
        
        # Add a marker for each province
        folium.Marker(
            location=[row['Lat'], row['Long_']],
            popup=f"{row['Province_State']}: {row['Confirmed']} confirmed cases",
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(pakistan_map)

    # Save the map to an HTML file
    map_file_path = 'pakistan_covid_map.html'
    pakistan_map.save(map_file_path)
    print(f"Map has been saved to '{map_file_path}'")

# Path to the provided Excel file containing the data
excel_path = 'combined_daily_reports.xlsx'

# Call the function with the path to the Excel file
plot_province_data_on_map(excel_path)
