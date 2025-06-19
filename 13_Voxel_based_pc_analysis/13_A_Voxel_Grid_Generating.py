#INFO *Der folgende Code wurde mithilfe von ChatGPT (OpenAI) erstellt und/oder bearbeitet.*

import laspy
import numpy as np
import open3d as o3d

def load_las_to_numpy(filepath):
    """Lädt eine LAS-Datei und gibt die XYZ-Koordinaten als NumPy-Array zurück."""
    las = laspy.read(filepath)
    points = np.vstack((las.x, las.y, las.z)).T
    return points

def create_voxel_grid(point_cloud_np, voxel_size=0.1, grid_origin=(0, 0, 0)):
    """Erzeugt ein Voxelgitter mit festem Ursprung aus Punktwolke."""
    points = point_cloud_np - grid_origin
    voxel_indices = np.floor(points / voxel_size).astype(np.int32)
    voxel_set = set(map(tuple, voxel_indices))
    return voxel_set, voxel_indices

def voxel_centers_from_indices(voxel_indices_set, voxel_size, grid_origin):
    """Berechnet die Mittelpunktkoordinaten der belegten Voxel."""
    voxel_indices_array = np.array(list(voxel_indices_set))
    centers = (voxel_indices_array + 0.5) * voxel_size + grid_origin
    return centers

def visualize_voxels(voxel_centers):
    """Zeigt das Voxelgitter mit Open3D an."""
    voxel_cloud = o3d.geometry.PointCloud()
    voxel_cloud.points = o3d.utility.Vector3dVector(voxel_centers)
    voxel_cloud.paint_uniform_color([1.0, 0.5, 0.0])
    o3d.visualization.draw_geometries([voxel_cloud])

# ------------------------------
# Parameter
voxel_size = 0.05  # Größe eines Voxels in Metern
grid_origin = np.array([2615390.524, 1264898.409, 280.00])  # Fester Startpunkt des Gitters
las_file_path = "F:\\50_Auswertung_PG\\500_Metashape\\5001_Kirsche\\20250423_DJIMini3Pro_Kirsche\\20250423_DJIMini3Pro_Kirsche_cleaned.las"  # Pfad zur LAS-Datei
# ------------------------------

# Schritt 1: LAS-Datei laden
points_np = load_las_to_numpy(las_file_path)

# Schritt 2: Voxelgitter erzeugen
voxel_set, voxel_indices = create_voxel_grid(points_np, voxel_size, grid_origin)

# Schritt 3: Mittelpunktkoordinaten der belegten Voxel berechnen
voxel_centers = voxel_centers_from_indices(voxel_set, voxel_size, grid_origin)

# Schritt 4: Visualisieren
visualize_voxels(voxel_centers)





