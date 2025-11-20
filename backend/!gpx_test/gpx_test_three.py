import gpxpy
import gpxpy.gpx
import math


# -----------------------
# Haversine (meters)
# -----------------------
def haversine(lat1, lon1, lat2, lon2):
    R = 6371000
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) *
         math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) ** 2)
    return 2 * R * math.asin(math.sqrt(a))


# -----------------------
# POI detection function
# -----------------------
def check_poi_matches(segment, poi_list, radius_m=100):
    """
    poi_list = [
        ['lat', 'lon', 'name'],
        ...
    ]
    """
    matches = []

    for raw_lat, raw_lon, name in poi_list:
        lat = float(raw_lat)
        lon = float(raw_lon)

        # Check each GPX point
        for p in segment.points:
            d = haversine(p.latitude, p.longitude, lat, lon)
            if d <= radius_m:
                matches.append((name, d))
                break  # Stop when first match is found

    return matches


# -----------------------
# Find closest POI to a single point
# -----------------------
def find_closest_poi(lat, lon, poi_list):
    """
    Returns (name, distance_m)
    """
    closest_name = None
    closest_distance = float("inf")

    for raw_lat, raw_lon, name in poi_list:
        d = haversine(lat, lon, float(raw_lat), float(raw_lon))
        if d < closest_distance:
            closest_distance = d
            closest_name = name

    return closest_name, closest_distance


# -----------------------
# Your main GPX processor
# -----------------------
def process_gpx(file_path="Test4.gpx", poi_list=None, poi_radius=100):

    with open(file_path, "r") as f:
        gpx = gpxpy.parse(f)

    track = gpx.tracks[0]
    segment = track.segments[0]

    # --- Distance ---
    distance_3d = segment.length_3d()

    # --- Elevation ---
    elevations = [p.elevation for p in segment.points if p.elevation is not None]
    total_ascent, total_descent = segment.get_uphill_downhill()
    max_ele = max(elevations) if elevations else None
    min_ele = min(elevations) if elevations else None

    # --- Moving data ---
    moving_data = segment.get_moving_data()
    moving_time, stopped_time, moving_distance, stopped_distance, max_speed = moving_data

    avg_speed_overall = distance_3d / (moving_time + stopped_time) if (moving_time + stopped_time) > 0 else 0
    avg_speed_moving = moving_distance / moving_time if moving_time > 0 else 0
    ascent_speed = (total_ascent / (moving_time / 3600)) if moving_time > 0 else 0

    # === Print your original results ===
    print("=== GPX Stats with gpxpy ===")
    print(f"Track name: {track.name}")
    print(f"Total points: {len(segment.points)}")
    print(f"Total distance: {distance_3d:.2f} m")
    print(f"Total ascent: {total_ascent:.2f} m")
    print(f"Total descent: {total_descent:.2f} m")
    print(f"Max elevation: {max_ele:.2f} m")
    print(f"Min elevation: {min_ele:.2f} m")
    print(f"Overall avg speed: {avg_speed_overall:.2f} m/s ({avg_speed_overall*3.6:.2f} km/h)")
    print(f"Moving avg speed: {avg_speed_moving:.2f} m/s ({avg_speed_moving*3.6:.2f} km/h)")
    print(f"Max speed: {max_speed:.2f} m/s ({max_speed*3.6:.2f} km/h)")
    print(f"Ascent speed: {ascent_speed:.2f} m/h")
    print(f"Moving time: {moving_time/60:.2f} min")
    print(f"Stopped time: {stopped_time/60:.2f} min")

    # --- POI detection along route ---
    if poi_list:
        matches = check_poi_matches(segment, poi_list, radius_m=poi_radius)

        print("\n=== POI Detection ===")
        print(f"Search radius: {poi_radius} meters\n")

        if not matches:
            print("No POIs found along this route.")
        else:
            for name, dist in matches:
                print(f" • {name}  (closest point {dist:.1f} m)")

        # --- Closest POI to start and end ---
        start_point = segment.points[0]
        end_point = segment.points[-1]

        start_closest, start_dist = find_closest_poi(start_point.latitude, start_point.longitude, poi_list)
        end_closest, end_dist = find_closest_poi(end_point.latitude, end_point.longitude, poi_list)

        print("\n=== Closest POIs ===")
        print(f"Start point closest to: {start_closest} ({start_dist:.1f} m)")
        print(f"End point closest to:   {end_closest} ({end_dist:.1f} m)")


# -----------------------
# Example usage
# -----------------------
points = [
    [47.175262, 8.516106, "zug station"],
    [47.177527, 8.516363, "Zug"],
    [47.154828, 8.543217, "Zugerberg"],
    [47.136391, 8.582373, "unterägeri"],
    [47.081728, 8.634016, "sattel"],
]

# Run
process_gpx("gpx/AAA.gpx", poi_list=points, poi_radius=100)
