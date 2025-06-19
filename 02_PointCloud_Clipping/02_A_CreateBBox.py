# INFO: *Der folgende Code wurde mithilfe von ChatGPT (OpenAI) erstellt und/oder bearbeitet.*

import geopandas as gpd
from shapely.geometry import box
from pathlib import Path

# === Werte der verschiedenen Bäume ===
#   Kirsche:
#   x_center = 2615390.524
#   y_center = 1264898.409

#   Ahorn:
#   x_center = 2615433.515
#   y_center = 1264855.159

#   Linde:
#   x_center = 2615380.973
#   y_center = 1264833.248



# === Parameter (hier anpassen) ===
x_center = 2615433.515
y_center = 1264855.159
buffer = 10
output_file = "Ahorn_10m.gpkg"
layer_name = "bbox"
crs = "EPSG:2056"

# === Bounding Box berechnen ===
half = buffer / 2.0
x_min, x_max = x_center - half, x_center + half
y_min, y_max = y_center - half, y_center + half
bbox_geom = box(x_min, y_min, x_max, y_max)

# === GeoDataFrame erstellen und speichern ===
gdf = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[bbox_geom])
gdf.to_file(Path(output_file), layer=layer_name, driver="GPKG")

print(f"GeoPackage gespeichert: {output_file}")
