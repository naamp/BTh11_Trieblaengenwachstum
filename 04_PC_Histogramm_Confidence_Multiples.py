import laspy
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.ticker import PercentFormatter
from tqdm import tqdm  # Ladebalken

# Liste der .las-Dateien im übergeordneten Verzeichnis
las_files = [
    "20250311_DJIMini3Pro_Kirsche_TiePointFiltering_20.las",
    "20250311_DJIMini3Pro_Kirsche_TiePointFiltering_40.las",
    "20250311_DJIMini3Pro_Kirsche_TiePointFiltering_60.las",
    "20250311_DJIMini3Pro_Kirsche_TiePointFiltering_80.las",
    "20250311_DJIMini3Pro_Kirsche_TiePointFiltering_100.las",
]

# Übergeordnetes Verzeichnis relativ zum Skript
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Plot-Layout vorbereiten
cols = 3
rows = (len(las_files) + cols - 1) // cols
fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 4 * rows))
axes = axes.flatten()

# Einheitliche y-Achse für Anteile in Prozent
y_max = 0.25  # max. 25 % pro Klasse

# Fortschrittsanzeige
for idx, file in enumerate(tqdm(las_files, desc="Verarbeite Punktwolken")):
    path = os.path.join(base_dir, file)
    
    try:
        las = laspy.read(path)
        confidence = las['confidence']
        label = file.split("_")[-1].replace(".las", "")

        # Statistiken berechnen
        mean_val = np.mean(confidence)
        median_val = np.median(confidence)
        above_10 = np.sum(confidence > 10) / len(confidence) * 100
        above_20 = np.sum(confidence > 20) / len(confidence) * 100

        # Plot
        ax = axes[idx]
        ax.hist(confidence, bins=20, density=True, alpha=0.75, color='gray', edgecolor='black')
        ax.set_title(
            f"TPF: {label}\nMittel: {mean_val:.2f}, Median: {median_val:.2f}\n"
            f">10: {above_10:.1f} %, >20: {above_20:.1f} %"
        )
        ax.set_xlabel("Confidence")
        ax.set_ylabel("Anteil Punkte")
        ax.set_ylim(0, y_max)
        ax.yaxis.set_major_formatter(PercentFormatter(xmax=1.0, decimals=0))
        ax.grid(True)

    except Exception as e:
        print(f"Fehler bei Datei {file}: {e}")
        axes[idx].set_visible(False)

# Leere Achsen ausblenden
for i in range(len(las_files), len(axes)):
    axes[i].set_visible(False)

fig.suptitle("Normierte Confidence-Histogramme aller Punktwolken mit Statistik", fontsize=16)
plt.tight_layout(rect=[0.03, 0.03, 1, 0.94])
plt.show()
