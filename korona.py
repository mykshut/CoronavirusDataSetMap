import pandas as pd
import folium

data = pd.read_csv("time_series_covid19_confirmed_global.csv")
lat = list(data["Lat"])
lon = list(data["Long"])
sum = list(data["4/3/20"])

def color_producer(people):
    if people < 1000:
        return "green"
    elif  1000 < people < 35000:
        return "orange"
    elif 35000 < people < 100000:
        return "red"
    else:
        return "brown"

def size_s(bim):
    if bim < 30:
        return 7
    elif  30 < bim < 100:
        return 9
    elif 101 < bim < 500:
        return 11
    else:
        return 13

map = folium.Map(location=[41.60335, 14.67607], zoom_start=2)
fg = folium.FeatureGroup(name="My map")

for lt, ln, sm in zip(lat, lon, sum):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=size_s(sm), popup=str(sm) + " confirmed coronavirus", tiles='CartoDB',
    fill_color=color_producer(sm), color="grey", fill_opacity=0.7))

map.add_child(fg)
map.save("coronavirus.html")

print("Your coronavirus online map > 'coronavirus.html' <  was succesfully added to the folder corona")
