# INFO: *Der folgende Code wurde mithilfe von ChatGPT (OpenAI) erstellt und/oder bearbeitet.*

import laspy
import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
from matplotlib.ticker import ScalarFormatter

# LAS-Dateien im übergeordneten Verzeichnis
las_files = [
    "20250311_DJIMini3Pro_Kirsche_TiePointFiltering_20_clipped.las",
    "20250311_DJIMini3Pro_Kirsche_TiePointFiltering_40_clipped.las",
    "20250311_DJIMini3Pro_Kirsche_TiePointFiltering_60_clipped.las",
    "20250311_DJIMini3Pro_Kirsche_TiePointFiltering_80_clipped.las",
    "20250311_DJIMini3Pro_Kirsche_TiePointFiltering_100_clipped.las",
]

# === Binning-Struktur: 1–1.99, ..., 11–11.99, >=12
bins = list(np.arange(1, 13, 1)) + [np.inf]
bin_labels = [f"{i}–{i+0.99}" for i in range(1, 12)] + [">=12"]

# Dictionary zum Speichern der normierten Verteilung (optional)
results = {label: [] for label in bin_labels}
labels_per_file = []

# Übergeordnetes Verzeichnis
base_dir = os.path.join(os.path.dirname(__file__), "clipped")

# Fortschrittsbalken für Analyse
for file in tqdm(las_files, desc="Analysiere Punktwolken"):
    path = os.path.join(base_dir, file)
    try:
        las = laspy.read(path)
        confidence = las['confidence']
        label = file.split("_")[-2].replace(".las", "")
        labels_per_file.append(label)

        # Histogramm (normiert) – nicht für Plot, aber falls du es später brauchst
        counts, _ = np.histogram(confidence, bins=bins)
        norm_counts = counts / np.sum(counts)
        for i, key in enumerate(bin_labels):
            results[key].append(norm_counts[i])

    except Exception as e:
        print(f"Fehler bei Datei {file}: {e}")
        for key in bin_labels:
            results[key].append(0)

# === Liniendiagramm: absolute Punktzahlen pro Kategorie ===
fig2, ax2 = plt.subplots(figsize=(14, 7))

# Anzahl der Datensätze (TPF-Stufen)
num_datasets = len(labels_per_file)

# Schutz bei leerer Analyse
if num_datasets == 0:
    print("Keine gültigen LAS-Dateien gefunden. Abbruch.")
    exit()

# Farben aus Colormap
cmap = plt.get_cmap("Blues")
colors = [cmap(0.4 + 0.6 * i / (num_datasets - 1)) for i in range(num_datasets)]

# Linien plotten
for i, label in enumerate(labels_per_file):
    path = os.path.join(base_dir, las_files[i])
    try:
        las = laspy.read(path)
        confidence = las['confidence']
        counts, _ = np.histogram(confidence, bins=bins)
        ax2.plot(bin_labels, counts, label=f"TPF {label}", color=colors[i], marker='o')
    except Exception as e:
        print(f"Fehler beim Lesen der Punktzahlen aus {las_files[i]}: {e}")

# Achsen & Formatierung
ax2.set_xlabel("Confidence-Kategorie")
ax2.set_ylabel("Anzahl Punkte")
ax2.set_title("Anzahl Punkte pro Confidence-Kategorie")
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend(title="Tie Point Filtering")

# Y-Achse im wissenschaftlichen Format
formatter = ScalarFormatter(useMathText=True)
formatter.set_powerlimits((6, 6))  # Zeigt ab 10^6 als Potenz
ax2.yaxis.set_major_formatter(formatter)
ax2.ticklabel_format(axis='y', style='sci')  # Aktiviert wissenschaftliche Schreibweise

plt.tight_layout()
plt.show()
