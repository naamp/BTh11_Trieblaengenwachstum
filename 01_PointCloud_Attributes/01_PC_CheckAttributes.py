import laspy
import pandas as pd
import os

# Parameter – Pfad zur Punktwolke
pc_path = r"C:\_Data\BTh11\BTh11_Trieblaengenwachstum\05_Software_Comparison\50_BaseData\PointCloud\20250326\20250326_DJIMini3Pro_Kirsche_Drone2Map_clipped.las"

# Cell 3: Punktwolke einlesen
try:
    las = laspy.read(pc_path)
    dims = list(las.point_format.dimension_names)
    print(f"Datei: {os.path.basename(pc_path)}")
    print(f"Anzahl Punkte: {len(las.points)}")
    print(f"Verfügbare Punktattribute: {dims}")
except Exception as e:
    print(f"Fehler beim Lesen der Datei: {e}")

# Cell 4: DataFrame der ersten 10 Werte aller Attribute erstellen
try:
    data = {}
    for dim in dims:
        try:
            values = getattr(las, dim)
            data[dim] = values[:10]
        except AttributeError:
            print(f"Attribut {dim} konnte nicht geladen werden.")
    
    df = pd.DataFrame(data)
    df
except Exception as e:
    print(f"Fehler beim Erstellen des DataFrames: {e}")