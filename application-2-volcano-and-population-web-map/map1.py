import folium

map = folium.Map(location=[41.8, -88.1], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[41.5, -88.5], popup="Downers Grove", icon=folium.Icon(color="green")))

map.add_child(fg)
map.save("/home/jose/Development/python-mega-course-build-10-real-world-applications/application-2-volcano-and-population-web-map/Map1.html")