import folium
import pandas

PROJECT_PATH = "/home/jose/Development/python-mega-course-build-10-real-world-applications/application-2-volcano-and-population-web-map/"
DATA_PATH = "/home/jose/Development/python-mega-course-build-10-real-world-applications/application-2-volcano-and-population-web-map/Volcanoes.txt"

volcano_data = pandas.read_csv(DATA_PATH)
lat  = list(volcano_data["LAT"])
lon  = list(volcano_data["LON"])
elev = list(volcano_data["ELEV"])
name = list(volcano_data["NAME"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[45, -121], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")
html = """
    <h4>Volcano information:</h4>
    Volcano name:<br>
    <a href="https://www.google.com/search?q=%s" target="_blank">%s</a><br>
    Height: %s m
"""

for lat, lon, elev, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, elev), width=200, height=100)
    
    fg.add_child(folium.CircleMarker(
            location=[lat, lon], 
            popup=folium.Popup(iframe),
            color="grey",
            fill=True,
            fill_color=color_producer(elev),
            radius=10.00,
            fill_opacity=0.7
        )
    )

map.add_child(fg)
map.save(PROJECT_PATH + "Map1.html")