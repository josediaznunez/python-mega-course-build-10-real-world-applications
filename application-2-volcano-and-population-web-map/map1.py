import folium
import pandas

PROJECT_PATH = "/home/jose/Development/python-mega-course-build-10-real-world-applications/application-2-volcano-and-population-web-map/"
DATA_PATH = "/home/jose/Development/python-mega-course-build-10-real-world-applications/application-2-volcano-and-population-web-map/Volcanoes.txt"

map = folium.Map(location=[45, -121], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

volcano_data = pandas.read_csv(DATA_PATH)
lat = list(volcano_data["LAT"])
lon = list(volcano_data["LON"])
elev = list(volcano_data["ELEV"])

for lat, lon, elev in zip(lat, lon, elev):
    fg.add_child(folium.Marker(
            location=[lat, lon], 
            popup=str(elev) + " m", 
            icon=folium.Icon(color="green")
        )
    )

map.add_child(fg)
map.save(PROJECT_PATH + "Map1.html")