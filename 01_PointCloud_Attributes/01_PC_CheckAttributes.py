import laspy
import os

# Absoluter Pfad zur LAS-Datei
pc_path = r"C:\_Data\BTh11\BTh11_Trieblaengenwachstum\05_Software_Comparison\50_BaseData\PointCloud\20250326\20250326_DJIMini3Pro_Kirsche_Drone2Map_clipped.las"

try:
    las = laspy.read(pc_path)
    dims = list(las.point_format.dimension_names)
    print(f"Datei: {os.path.basename(pc_path)}")
    print("Verfügbare Punktattribute und erste 10 Werte:")
    
    for dim in dims:
        try:
            values = getattr(las, dim)
            print(f"\nAttribut: {dim}")
            print(values[:10])  # Zeige die ersten 10 Werte
        except AttributeError:
            print(f"\nAttribut: {dim} konnte nicht ausgelesen werden.")
except Exception as e:
    print(f"Fehler beim Lesen der Datei: {e}")
