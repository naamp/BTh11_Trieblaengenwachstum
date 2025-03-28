import laspy
import os

# Liste der LAS-Dateien im übergeordneten Verzeichnis
las_files = [
    "20250311_DJIMini3Pro_Kirsche_TiePointFiltering_20.las",
    "20250311_DJIMini3Pro_Kirsche_TiePointFiltering_40.las",
    "20250311_DJIMini3Pro_Kirsche_TiePointFiltering_60.las",
    "20250311_DJIMini3Pro_Kirsche_TiePointFiltering_80.las",
    "20250311_DJIMini3Pro_Kirsche_TiePointFiltering_100.las",
]

# Basisverzeichnis: ein Ordner über dem aktuellen Skript
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

for file in las_files:
    path = os.path.join(base_dir, file)
    
    try:
        las = laspy.read(path)
        dims = list(las.point_format.dimension_names)
        print(f"Datei: {file}")
        print("Verfügbare Punktattribute:")
        print(dims)
        print("-" * 40)
    except Exception as e:
        print(f"Fehler beim Lesen von {file}: {e}")
