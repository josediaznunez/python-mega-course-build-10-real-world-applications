import folium

PROJECT_PATH = "/home/jose/Development/python-mega-course-build-10-real-world-applications/application-2-volcano-and-population-web-map/"

map = folium.Map(location=[41.8, -88.1], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
for coordinates in [[42.5, -87.5], [43.5, -86.5]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Downers Grove", icon=folium.Icon(color="green")))

map.add_child(fg)
map.save(PROJECT_PATH + "Map1.html")