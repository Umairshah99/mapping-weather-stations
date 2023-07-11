import pandas as pd
import folium

#Open Sense Weather Stations
# Read file into a pandas DataFrame
data = pd.read_csv('open_sense_weather_stations.csv')
data = data.dropna()
max_range = len(data)

# Create a folium map centered on the first latitude and longitude
map_center = [data['Latitude'].iloc[0], data['Longitude'].iloc[0]]
m2 = folium.Map(location=map_center, tiles='cartodbpositron', zoom_start=2)

# Iterate over the rows and add markers to the map
for i in range(0, max_range):
    latitude = data['Latitude'].iloc[i]
    longitude = data['Longitude'].iloc[i]    
    marker = folium.CircleMarker(location=[latitude, longitude],
                        radius=3,
                        weight=3,
                        popup='<table><tr><th>OS Name</th><th>'+str(data['Name'].iloc[i])+'</th></tr><tbody><tr><td>Latitude</td><td>'+str(latitude)+'</td></tr><tr><td>Longitude</td><td>'+str(longitude)+'</td></tr></tbody></table>'
)

    marker.add_to(m2)



#Smart Citizen Weather Stations
data = pd.read_csv('smart_citizen_weather_stations.csv')
data = data.dropna()

max_range = len(data)
    
for i in range(0, max_range):
    latitude = data['Latitude'].iloc[i]
    longitude = data['Longitude'].iloc[i]    
    marker = folium.CircleMarker(location=[latitude, longitude],
                        color='red',
                        radius=3,
                        weight=3,
                        popup='<table><tr><th>SC Name</th><th>'+str(data['Name_Code'].iloc[i])+'</th></tr><tbody><tr><td>Latitude</td><td>'+str(latitude)+'</td></tr><tr><td>Longitude</td><td>'+str(longitude)+'</td></tr></tbody></table>'
)

    marker.add_to(m2)
    


data = pd.read_csv('site_list_towns_en.csv')
data = data.dropna()

max_range = len(data)
    
for i in range(0, max_range):
    latitude = data['Latitude'].iloc[i]
    longitude = data['Longitude'].iloc[i]    
    marker = folium.CircleMarker(location=[latitude[:-1], -float(longitude[:-1])],
                        color='green',
                        radius=3,
                        weight=3,
                        popup='<table><tr><th>CA Name</th><th>'+str(data['English Names'].iloc[i])+'</th></tr><tbody><tr><td>Latitude</td><td>'+str(latitude)+'</td></tr><tr><td>Longitude</td><td>'+str(longitude)+'</td></tr></tbody></table>'
)

    marker.add_to(m2)
    

#Add more as above for a map with all the covered data
m2.save('combined_demo.html')