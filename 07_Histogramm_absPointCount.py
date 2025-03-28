import laspy
import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
from matplotlib.ticker import ScalarFormatter

# === LAS-Dateien mit TPF-Stufen ===
las_files = [
    "20250311_DJIMini3Pro_Kirsche_TiePointFiltering_20_clipped.las",
    "20250311_DJIMini3Pro_Kirsche_TiePointFiltering_40_clipped.las",
    "20250311_DJIMini3Pro_Kirsche_TiePointFiltering_60_clipped.las",
    "20250311_DJIMini3Pro_Kirsche_TiePointFiltering_80_clipped.las",
    "20250311_DJIMini3Pro_Kirsche_TiePointFiltering_100_clipped.las",
]

# === Verzeichnis mit den .las-Dateien ===
base_dir = os.path.join(os.path.dirname(__file__), "clipped")

# === Punktanzahl pro Datei erfassen ===
labels = []
point_counts = []

for file in tqdm(las_files, desc="Zähle Punkte"):
    path = os.path.join(base_dir, file)
    try:
        las = laspy.read(path)
        count = len(las.points)
        point_counts.append(count)

        # TPF-Stufe aus Dateiname extrahieren
        label = file.split("_")[-2]
        labels.append(f"TPF {label}")

    except Exception as e:
        print(f"Fehler beim Lesen der Datei {file}: {e}")
        labels.append("Fehler")
        point_counts.append(0)

# === Farbabstufung berechnen ===
num_datasets = len(labels)
cmap = plt.get_cmap("Blues")
colors = [cmap(0.4 + 0.6 * i / (num_datasets - 1)) for i in range(num_datasets)]

# === Balkendiagramm erstellen ===
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(labels, point_counts, color=colors)

# Achsenbeschriftung und Formatierung
ax.set_title("Anzahl Punkte pro Punktwolke (TPF-Stufen)")
ax.set_xlabel("Tie Point Filtering")
ax.set_ylabel("Anzahl Punkte")
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Y-Achse im wissenschaftlichen Format (× 10⁸)
formatter = ScalarFormatter(useMathText=True)
formatter.set_powerlimits((6, 6))
ax.yaxis.set_major_formatter(formatter)
ax.ticklabel_format(axis='y', style='sci')
ax.yaxis.offsetText.set_visible(True)

plt.tight_layout()
plt.show()
