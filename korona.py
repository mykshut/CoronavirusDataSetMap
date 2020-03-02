import pandas as pd
import folium

data = pd.read_csv("time_series_19-covid-Recovered.csv")
lat = list(data["Lat"])
lon = list(data["Long"])
sum = list(data["SUM"])

def color_producer(people):
    if people < 30:
        return "green"
    elif  30 < people < 100:
        return "orange"
    elif 101 < people < 500:
        return "red"
    else:
        return "brown"

def size_s(bim):
    if bim < 30:
        return 5
    elif  30 < bim < 100:
        return 7
    elif 101 < bim < 500:
        return 10
    else:
        return 12

map = folium.Map(location=[41.60335, 14.67607], zoom_start=2)
fg = folium.FeatureGroup(name="My map")

for lt, ln, sm in zip(lat, lon, sum):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=size_s(sm), popup=str(sm) + " have coronavirus",
    fill_color=color_producer(sm), color="grey", fill_opacity=0.7))

map.add_child(fg)
map.save("coronavirus.html")

print("Your project coronavirus.html was succesfully added to the folder korona")
