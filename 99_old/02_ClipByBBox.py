import laspy
import geopandas as gpd
import numpy as np
from shapely.geometry import Point
from pathlib import Path
from tqdm import tqdm

# === Parameter (hier anpassen) ===
las_file = Path("../20250311_DJIMini3Pro_Kirsche_TiePointFiltering_20.las")
gpkg_file = Path("Kirsche_10m.gpkg")
layer_name = "bbox"
output_file = Path("clipped/20250311_DJIMini3Pro_Kirsche_TiePointFiltering_20_clipped.las")

# === GeoPackage laden ===
gdf = gpd.read_file(gpkg_file, layer=layer_name)
if gdf.empty:
    print("GeoPackage enthält keine Geometrien.")
    exit()

bbox_geom = gdf.geometry.union_all()

# === LAS-Datei lesen ===
las = laspy.read(las_file)
x = las.x
y = las.y

print(f"Prüfe {len(x):,} Punkte gegen Geometrie...")

# Ladebalken für Punkt-in-Polygon-Test
points = [Point(x[i], y[i]) for i in tqdm(range(len(x)), desc="Punkt-in-Polygon")]
mask = np.array([bbox_geom.contains(pt) for pt in tqdm(points, desc="Maske erstellen")])

if not mask.any():
    print("Keine Punkte innerhalb der Bounding Box gefunden.")
    exit()

# Neue Punktwolke mit gefilterten Punkten
header = las.header.copy()
clipped_las = laspy.LasData(header)

for dim in las.point_format.dimension_names:
    clipped_las[dim] = las[dim][mask]

output_file.parent.mkdir(exist_ok=True)
clipped_las.write(output_file)

print(f"Geschnittene Punktwolke gespeichert unter: {output_file}")
