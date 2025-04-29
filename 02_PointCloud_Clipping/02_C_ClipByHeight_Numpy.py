import laspy
import numpy as np
from pathlib import Path

# === Parameter (hier anpassen) ===

las_file = Path(r"D:\BTh11_Asuwertung_PC\fhnw_code\BTh11_Trieblaengenwachstum\06_UAV_Comparison\60_BaseData\PointCloud\20250326_DJIMini3Pro_Kirsche_clipped.las")
output_file = Path(r"D:\BTh11_Asuwertung_PC\fhnw_code\BTh11_Trieblaengenwachstum\06_UAV_Comparison\60_BaseData\PointCloud\pc_tree\20250326_DJIMini3Pro_Kirsche_clipped_tree.las")

# Höhenfilter: Nur Punkte oberhalb dieser Höhe (in denselben Einheiten wie Z im LAS-File)

# === Werte der verschiedenen Bäume ===
height_kirsche = 280.00
height_ahorn = 278.80
height_linde = 280.50


min_height = height_kirsche # Hier Variable anpassen je nach Baum!!!!

# === LAS-Datei lesen ===
las = laspy.read(las_file)
z = las.z

# Filtermaske: Nur Punkte oberhalb der angegebenen Höhe behalten
mask = z >= min_height

if not mask.any():
    print("Keine Punkte oberhalb der angegebenen Höhe gefunden.")
    exit()

# Neue Punktwolke mit gefilterten Punkten
clipped_las = laspy.LasData(las.header)
clipped_las.points = las.points[mask]

# Ausgabeordner erstellen, falls nicht vorhanden
output_file.parent.mkdir(exist_ok=True)

# Neue Datei speichern
clipped_las.write(output_file)

print(f"Punktwolke nach Höhenfilter gespeichert unter: {output_file}")
