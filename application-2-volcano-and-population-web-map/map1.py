import folium
import pandas

PROJECT_PATH = "/home/jose/Development/python-mega-course-build-10-real-world-applications/application-2-volcano-and-population-web-map/"
DATA_PATH = "/home/jose/Development/python-mega-course-build-10-real-world-applications/application-2-volcano-and-population-web-map/Volcanoes.txt"

volcano_data = pandas.read_csv(DATA_PATH)
lat = list(volcano_data["LAT"])
lon = list(volcano_data["LON"])
elev = list(volcano_data["ELEV"])

map = folium.Map(location=[45, -121], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")
html = """<h4>Volcano information:</h4>Height: %s m"""

for lat, lon, elev in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(elev), width=200, height=100)
    fg.add_child(folium.Marker(
            location=[lat, lon], 
            popup=folium.Popup(iframe),
            icon=folium.Icon(color="green")
        )
    )

map.add_child(fg)
map.save(PROJECT_PATH + "Map1.html")