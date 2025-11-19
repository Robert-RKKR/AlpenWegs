import gpxpy
import numpy as np
from scipy.spatial import KDTree
import math


def load_gpx_points(path):
    with open(path, "r") as f:
        gpx = gpxpy.parse(f)
    seg = gpx.tracks[0].segments[0]
    pts = [(p.latitude, p.longitude, p.elevation or 0) for p in seg.points]
    return np.array(pts)


def haversine_vec(lat1, lon1, lat2, lon2):
    R = 6371000
    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)
    a = (np.sin(dlat/2) ** 2 +
         np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon/2)**2)
    return 2 * R * np.arcsin(np.sqrt(a))


def latlon_to_xyz(lat, lon):
    # convert to 3D cartesian for KDTree stability
    lat_r, lon_r = np.radians(lat), np.radians(lon)
    R = 6371000
    x = R * np.cos(lat_r) * np.cos(lon_r)
    y = R * np.cos(lat_r) * np.sin(lon_r)
    z = R * np.sin(lat_r)
    return np.vstack((x, y, z)).T


def compare_gpx(file_a, file_b, tolerance_m=25):
    pts_a = load_gpx_points(file_a)
    pts_b = load_gpx_points(file_b)

    # KD-tree on B
    xyz_b = latlon_to_xyz(pts_b[:, 0], pts_b[:, 1])
    tree = KDTree(xyz_b)

    xyz_a = latlon_to_xyz(pts_a[:, 0], pts_a[:, 1])
    dist_xyz, idx = tree.query(xyz_a, k=1)

    # Convert xyz distance to meters using haversine for accuracy
    nearest = pts_b[idx]
    dist_m = haversine_vec(
        pts_a[:, 0], pts_a[:, 1],
        nearest[:, 0], nearest[:, 1]
    )

    matched = np.sum(dist_m <= tolerance_m)
    proximity_sim = matched / len(pts_a) * 100

    # Distance similarity
    # (crude but effective)
    dist_a = len(pts_a)
    dist_b = len(pts_b)
    distance_sim = min(dist_a, dist_b) / max(dist_a, dist_b) * 100

    # Elevation correlation
    ele_a = pts_a[:, 2]
    ele_b = pts_b[:, 2]
    ele_corr = np.corrcoef(ele_a[:min(len(ele_a), len(ele_b))],
                           ele_b[:min(len(ele_a), len(ele_b))])[0, 1]
    elevation_sim = max(0, (ele_corr + 1) / 2 * 100)

    # Final score
    final = (
        0.60 * proximity_sim +
        0.20 * distance_sim +
        0.20 * elevation_sim
    )

    return {
        "proximity_similarity": round(proximity_sim, 2),
        "distance_similarity": round(distance_sim, 2),
        "elevation_similarity": round(elevation_sim, 2),
        "final_similarity_score": round(final, 2),
        "matched_points": int(matched),
        "total_points": int(len(pts_a)),
        "tolerance_m": tolerance_m,
    }


def print_similarity(result):
    print("\n=== GPX ROUTE SIMILARITY REPORT ===")
    print(f"Tolerance distance: {result['tolerance_m']} m\n")
    print(f"Route corridor similarity:   {result['proximity_similarity']:.2f}%")
    print(f"Distance similarity:         {result['distance_similarity']:.2f}%")
    print(f"Elevation similarity:        {result['elevation_similarity']:.2f}%")
    print("--------------------------------------------------")
    print(f"FINAL ROUTE SIMILARITY:      {result['final_similarity_score']:.2f}%")
    print("--------------------------------------------------")
    print(f"Matched points: {result['matched_points']} / {result['total_points']}")
    print("==============================================\n")


# Example
result = compare_gpx("AAA.gpx", "BBB.gpx", tolerance_m=25)
print_similarity(result)
