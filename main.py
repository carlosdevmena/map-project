import folium
import pandas as pd

# Cargar los datos de ubicación
data = pd.read_csv("direccion.csv")

# Crear un mapa
mapa = folium.Map()

# Agregar los datos de ubicación al mapa
for index, row in data.iterrows():
    folium.Marker(location=[row["lat"], row["lon"]], popup=row["name"]).add_to(mapa)

# Mostrar el mapa
mapa.save("mapa.html")