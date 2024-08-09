import folium

# Center of the map on Lagos, Nigeria
map_center = [6.5244, 3.3792]
mymap = folium.Map(location=map_center, zoom_start=12)

# Adding a marker to Lagos
folium.Marker(
    [6.5244, 3.3792],
    popup='Lagos',
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(mymap)

# Save the map to an HTML file
mymap.save('lagos_map.html')

# Now open 'lagos_map.html' in your web browser
