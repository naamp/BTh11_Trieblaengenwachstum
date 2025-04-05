import laspy
import geopandas as gpd
import numpy as np
from pathlib import Path

# === Parameter (hier anpassen) ===
print("CLipping gestartet")
las_file = Path("D:\\BTh11_Asuwertung_PC\\05_Datenprozessierung\\50_Auswertung_PG\\20250326_DJIMini3Pro_Kirsche_pointcloud.las")
gpkg_file = Path("D:\\BTh11_Asuwertung_PC\\fhnw_code\\BTh11_Trieblaengenwachstum\\02_PointCloud_Clipping\\02_BBox_Data\\Kirsche_10m.gpkg")
layer_name = "bbox"
output_file = Path("D:\\BTh11_Asuwertung_PC\\fhnw_code\\BTh11_Trieblaengenwachstum\\06_UAV_Comparison\\60_BaseData\\PointCloud\\20250326_DJIMini3Pro_Kirsche_clipped.las")
print("Pfade gelesen")
# === GeoPackage laden und Bounding Box extrahieren ===
gdf = gpd.read_file(gpkg_file, layer=layer_name)
if gdf.empty:
    print("GeoPackage enthält keine Geometrien.")
    exit()

bbox = gdf.geometry.total_bounds  # [minx, miny, maxx, maxy]
x_min, y_min, x_max, y_max = bbox

# === LAS-Datei lesen ===
las = laspy.read(las_file)
x = las.x
y = las.y

# vektorbasierter Bounding-Box-Filter für Quadrate
mask = (x >= x_min) & (x <= x_max) & (y >= y_min) & (y <= y_max)

if not mask.any():
    print("Keine Punkte innerhalb der Bounding Box gefunden.")
    exit()

# Neue Punktwolke mit gefilterten Punkten
clipped_las = laspy.LasData(las.header)
clipped_las.points = las.points[mask]

output_file.parent.mkdir(exist_ok=True)
clipped_las.write(output_file)

print(f"Geschnittene Punktwolke gespeichert unter: {output_file}")
