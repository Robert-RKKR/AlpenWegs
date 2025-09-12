import gpxpy
import gpxpy.gpx


def process_gpx(file_path="Test4.gpx"):
    with open(file_path, "r") as f:
        gpx = gpxpy.parse(f)

    # For simplicity, use the first track and first segment
    track = gpx.tracks[0]
    segment = track.segments[0]

    # --- Distance ---
    distance_3d = segment.length_3d()  # meters

    # --- Elevation stats ---
    elevations = [p.elevation for p in segment.points if p.elevation is not None]
    total_ascent, total_descent = segment.get_uphill_downhill()
    max_ele = max(elevations) if elevations else None
    min_ele = min(elevations) if elevations else None

    # --- Moving data (speed, times) ---
    moving_data = segment.get_moving_data()  # returns (moving_time, stopped_time, moving_distance, stopped_distance, max_speed)
    moving_time, stopped_time, moving_distance, stopped_distance, max_speed = moving_data

    # Average speeds
    avg_speed_overall = distance_3d / (moving_time + stopped_time) if (moving_time + stopped_time) > 0 else 0
    avg_speed_moving = moving_distance / moving_time if moving_time > 0 else 0

    # --- Ascent speed (vertical meters per hour) ---
    ascent_speed = (total_ascent / (moving_time / 3600)) if moving_time > 0 else 0

    # --- Print results ---
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


# Run on your GPX file
process_gpx("Test1.gpx")
