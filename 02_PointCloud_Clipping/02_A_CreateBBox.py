import geopandas as gpd
from shapely.geometry import box
from pathlib import Path

# === Parameter (hier anpassen) ===
x_center = 2615390.524
y_center = 1264898.409
buffer = 10
output_file = "Kirsche_10m.gpkg"
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
