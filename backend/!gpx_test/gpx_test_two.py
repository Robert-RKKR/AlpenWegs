import time
import gpxpy
import gpxpy.gpx
from ezgpx import GPX


# -------------------------------------------------------------
# Helper
# -------------------------------------------------------------
def safe(value, digits=2):
    try:
        return round(float(value), digits)
    except Exception:
        return None


# =============================================================
# ezGPX PROCESSOR  (SAFE VERSION)
# =============================================================
def process_with_ezgpx(file_path="Test.gpx"):
    start_time = time.perf_counter()
    gpx = GPX(file_path)

    total_points = gpx.nb_points()
    total_distance = gpx.distance()
    ascent = gpx.ascent()
    descent = gpx.descent()
    max_ele = gpx.max_elevation()
    min_ele = gpx.min_elevation()

    # Extract points safely
    try:
        track = gpx.tracks[0]
        segment = track.segments[0]
        points = segment.points
    except Exception:
        points = []

    has_time = any(p.time is not None for p in points)

    overall_avg = None
    moving_avg = None
    max_speed = None
    ascent_speed = None
    moving_time = None
    stopped_time = None

    # Compute speed/time only if timestamps exist
    if has_time and len(points) >= 2:
        speeds = []
        moving_time_sec = 0.0
        stopped_time_sec = 0.0

        for p1, p2 in zip(points[:-1], points[1:]):
            if p1.time is None or p2.time is None:
                continue

            dt = (p2.time - p1.time).total_seconds()
            if dt <= 0:
                continue

            dist = p1.distance_3d(p2)
            speed = dist / dt
            speeds.append(speed)

            if speed > 0.5:
                moving_time_sec += dt
            else:
                stopped_time_sec += dt

        if speeds:
            moving_avg = sum(speeds) / len(speeds)
            max_speed = max(speeds)

        total_time_sec = moving_time_sec + stopped_time_sec
        if total_time_sec > 0 and total_distance > 0:
            overall_avg = total_distance / total_time_sec

        moving_time = moving_time_sec
        stopped_time = stopped_time_sec

        if moving_time_sec > 0:
            ascent_speed = (ascent / moving_time_sec) * 3600

    execution_time = time.perf_counter() - start_time

    return {
        "Name": gpx.name(),
        "Total Points": total_points,
        "Total Distance (m)": safe(total_distance),
        "Total Ascent (m)": safe(ascent),
        "Total Descent (m)": safe(descent),
        "Max Elevation (m)": safe(max_ele),
        "Min Elevation (m)": safe(min_ele),
        "Overall Avg Speed (m/s)": safe(overall_avg),
        "Moving Avg Speed (m/s)": safe(moving_avg),
        "Max Speed (m/s)": safe(max_speed),
        "Ascent Speed (m/h)": safe(ascent_speed),
        "Moving Time (s)": safe(moving_time),
        "Stopped Time (s)": safe(stopped_time),
        "Execution Time (s)": safe(execution_time, 4),
    }


# =============================================================
# GPXPY PROCESSOR with SAFE UNPACKING
# =============================================================
def process_with_gpxpy(file_path="Test.gpx"):
    start_time = time.perf_counter()

    with open(file_path, "r") as f:
        gpx = gpxpy.parse(f)

    track = gpx.tracks[0]
    segment = track.segments[0]
    points = segment.points

    elevations = [p.elevation for p in points if p.elevation is not None]
    max_ele = max(elevations) if elevations else None
    min_ele = min(elevations) if elevations else None

    distance_3d = segment.length_3d()

    uphill, downhill = segment.get_uphill_downhill()

    # ---------------------------------------------------------
    # SAFE HANDLING OF DIFFERENT GPXPY RETURN FORMATS
    # ---------------------------------------------------------
    moving_data = segment.get_moving_data()

    # newer versions: (moving_time, stopped_time, moving_distance, max_speed)
    # older versions: (moving_time, stopped_time, max_speed)
    if len(moving_data) == 4:
        moving_time, stopped_time, moving_distance, max_speed = moving_data
    elif len(moving_data) == 3:
        moving_time, stopped_time, max_speed = moving_data
        moving_distance = None
    else:
        moving_time = stopped_time = moving_distance = max_speed = None

    # Speed averages safely
    try:
        avg_overall_speed, avg_moving_speed = segment.get_speed_data()
    except Exception:
        avg_overall_speed = None
        avg_moving_speed = None

    ascent_speed = None
    if moving_time and moving_time > 0:
        ascent_speed = (uphill / moving_time) * 3600

    execution_time = time.perf_counter() - start_time

    return {
        "Name": track.name or "N/A",
        "Total Points": len(points),
        "Total Distance (m)": safe(distance_3d),
        "Total Ascent (m)": safe(uphill),
        "Total Descent (m)": safe(downhill),
        "Max Elevation (m)": safe(max_ele),
        "Min Elevation (m)": safe(min_ele),
        "Overall Avg Speed (m/s)": safe(avg_overall_speed),
        "Moving Avg Speed (m/s)": safe(avg_moving_speed),
        "Max Speed (m/s)": safe(max_speed),
        "Ascent Speed (m/h)": safe(ascent_speed),
        "Moving Time (s)": safe(moving_time),
        "Stopped Time (s)": safe(stopped_time),
        "Execution Time (s)": safe(execution_time, 4),
    }


# =============================================================
# COMPARISON OUTPUT
# =============================================================
def process_gpx(file_path="Test.gpx"):
    print(f"\n===== Processing: {file_path} =====")

    ezgpx_data = process_with_ezgpx(file_path)
    gpxpy_data = process_with_gpxpy(file_path)

    print("\n=== ezGPX Stats ===")
    for k, v in ezgpx_data.items():
        print(f"{k}: {v}")

    print("\n=== gpxpy Stats ===")
    for k, v in gpxpy_data.items():
        print(f"{k}: {v}")

    # ---------------------------------------------------------
    # NEW COMPARISON FORMAT WITH DIFFERENCE
    # ---------------------------------------------------------
    print("\n=== Comparison (ezGPX vs gpxpy) ===")
    for key in ezgpx_data:
        if key == "Execution Time (s)":
            continue

        val_ez = ezgpx_data[key]
        val_py = gpxpy_data[key]

        # Compute absolute difference if both are numbers
        if isinstance(val_ez, (int, float)) and isinstance(val_py, (int, float)):
            diff = round(abs(val_ez - val_py), 2)
        else:
            diff = "N/A"

        print(f"{key}: {val_ez} | {val_py} | {diff}")

    print("\n=== Execution Time Comparison ===")
    print(f"ezGPX: {ezgpx_data['Execution Time (s)']} s")
    print(f"gpxpy: {gpxpy_data['Execution Time (s)']} s")

    print("========================================\n")


# =============================================================
# RUNNER
# =============================================================
if __name__ == "__main__":

    print("\nProcessing AAA.gpx")
    process_gpx("gpx/AAA.gpx")

    print("\nProcessing DDD.gpx")
    process_gpx("gpx/DDD.gpx")

    print("\nProcessing VoieVerteHauteVosges.gpx")
    process_gpx("gpx/VoieVerteHauteVosges.gpx")
