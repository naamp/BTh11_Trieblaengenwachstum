import laspy
import geopandas as gpd
import numpy as np
from pathlib import Path

# EINGABE Parameter ===

las_file = Path(r"G:\52_Vollstaendigkeitspruefung\20250319_RTC360_Kirsche_clipped_1.las")
gpkg_file = Path(r"C:\_Data\BTh11\BTh11_Trieblaengenwachstum\02_PointCloud_Clipping\02_BBox_Data\Kirsche_10m.gpkg")
layer_name = "bbox"
output_file = Path(r"G:\52_Vollstaendigkeitspruefung\20250326_DJIMini3Pro_Kirsche\20250319_RTC360_Kirsche_clipped.las")

# === Werte der verschiedenen Bäume ===
height_kirsche = 280.00
height_ahorn = 278.80
height_linde = 280.50

# EINGABE Variable, Anpassen je nach Baum!!!!
min_height = height_kirsche 

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
z = las.z

# Kombinierter Filter: Bounding Box UND Höhenfilter
mask = (
    (x >= x_min) & (x <= x_max) &
    (y >= y_min) & (y <= y_max) &
    (z >= min_height)
)

if not mask.any():
    print("Keine Punkte innerhalb der Bounding Box und oberhalb der Mindesthöhe gefunden.")
    exit()

# Neue Punktwolke mit gefilterten Punkten
clipped_las = laspy.LasData(las.header)
clipped_las.points = las.points[mask]

# Sicherstellen, dass Zielverzeichnis existiert
output_file.parent.mkdir(exist_ok=True)

# Datei schreiben
clipped_las.write(output_file)

print(f"Punktwolke erfolgreich gespeichert unter: {output_file}")
