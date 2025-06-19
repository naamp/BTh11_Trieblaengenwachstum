# INFO: *Der folgende Code wurde mithilfe von ChatGPT (OpenAI) erstellt und/oder bearbeitet.*

import laspy
import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm

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

# Dictionary zum Speichern der Ergebnisse
results = {label: [] for label in bin_labels}
labels_per_file = []

# Übergeordnetes Verzeichnis
base_dir = os.path.join(os.path.dirname(__file__), "clipped")

# Analyse mit Fortschrittsbalken
for file in tqdm(las_files, desc="Analysiere Punktwolken"):
    path = os.path.join(base_dir, file)
    try:
        las = laspy.read(path)
        confidence = las['confidence']
        label = file.split("_")[-2].replace(".las", "")
        labels_per_file.append(label)

        # Histogramm nach Kategorien (absolute Werte)
        counts, _ = np.histogram(confidence, bins=bins)

        # Normieren auf Summe = 1
        norm_counts = counts / np.sum(counts)

        for i, key in enumerate(bin_labels):
            results[key].append(norm_counts[i])

    except Exception as e:
        print(f"Fehler bei Datei {file}: {e}")
        for key in bin_labels:
            results[key].append(0)

# Balkendiagramm: nebeneinander
num_datasets = len(labels_per_file)
num_bins = len(bin_labels)

# Schutz bei leerer Analyse
if num_datasets == 0:
    print("Keine gültigen LAS-Dateien gefunden. Abbruch.")
    exit()

x = np.arange(num_bins)
width = 0.8 / num_datasets

fig, ax = plt.subplots(figsize=(14, 7))

# Farben generieren aus der Colormap 'Blues'
cmap = plt.get_cmap("Blues")
colors = [cmap(0.4 + 0.6 * i / (num_datasets - 1)) for i in range(num_datasets)]

for i, label in enumerate(labels_per_file):
    offsets = x + i * width - (width * (num_datasets - 1) / 2)
    heights = [results[cat][i] for cat in bin_labels]
    ax.bar(offsets, heights, width=width, label=f'TPF {label}', color=colors[i])

ax.set_xticks(x)
ax.set_xticklabels(bin_labels, rotation=45, ha="right")
ax.set_xlabel("Confidence-Kategorie")
ax.set_ylabel("Anteil verbleibende Punkte [%]")
ax.set_ylim(0, 1)
ax.set_yticks(np.arange(0, 1.1, 0.1))
ax.set_title("Vergleich der normierten Confidence-Verteilung")
ax.legend(title="Tie Point Filtering")
ax.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
