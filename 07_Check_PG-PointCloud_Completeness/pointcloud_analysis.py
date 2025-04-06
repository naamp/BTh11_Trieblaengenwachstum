
import open3d as o3d
import numpy as np
import laspy

def read_las_to_pcd(path):
    las = laspy.read(path)
    points = np.vstack((las.x, las.y, las.z)).transpose()
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    return pcd

def remove_ground(pcd, height_threshold=0.05):
    z_values = np.asarray(pcd.points)[:, 2]
    mask = z_values > (np.min(z_values) + height_threshold)
    pcd_filtered = pcd.select_by_index(np.where(mask)[0])
    return pcd_filtered

def voxel_completeness(pcd_ref, pcd_test, voxel_size=0.001):
    voxel_grid_ref = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd_ref, voxel_size)
    voxel_grid_test = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd_test, voxel_size)

    occupied_voxels_ref = set([v.grid_index for v in voxel_grid_ref.get_voxels()])
    occupied_voxels_test = set([v.grid_index for v in voxel_grid_test.get_voxels()])

    intersection = occupied_voxels_ref.intersection(occupied_voxels_test)

    completeness_ratio = len(intersection) / len(occupied_voxels_ref) * 100
    return completeness_ratio

def c2c_statistics(pcd_src, pcd_tgt):
    pcd_tree = o3d.geometry.KDTreeFlann(pcd_tgt)
    distances = []

    for point in pcd_src.points:
        [_, idx, distsq] = pcd_tree.search_knn_vector_3d(point, 1)
        distances.append(np.sqrt(distsq[0]))

    distances = np.array(distances)
    return {
        'mean': np.mean(distances),
        'std': np.std(distances),
        'rmse': np.sqrt(np.mean(distances**2)),
        'max': np.max(distances),
        'min': np.min(distances),
        'count': len(distances),
        'distances': distances
    }
