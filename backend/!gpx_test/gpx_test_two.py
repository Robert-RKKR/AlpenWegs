import time
import gpxpy
import gpxpy.gpx
from ezgpx import GPX


def process_with_ezgpx(file_path="Test.gpx"):
    start_time = time.perf_counter()

    gpx = GPX(file_path)

    results = {
        "Name": gpx.name(),
        "Total Points": gpx.nb_points(),
        "Total Distance (m)": round(gpx.distance(), 2),
        "Total Ascent (m)": round(gpx.ascent(), 2),
        "Total Descent (m)": round(gpx.descent(), 2),
        "Max Elevation (m)": round(gpx.max_elevation(), 2),
    }

    print(f'avg_moving_pace: {gpx.compute_points_ascent_rate()}')


    execution_time = time.perf_counter() - start_time
    results["Execution Time (s)"] = round(execution_time, 4)
    return results


def process_with_gpxpy(file_path="Test.gpx"):
    start_time = time.perf_counter()

    with open(file_path, "r") as f:
        gpx = gpxpy.parse(f)

    # Use only first track/segment
    track = gpx.tracks[0]
    segment = track.segments[0]

    results = {
        "Name": track.name or "N/A",
        "Total Points": len(segment.points),
        "Total Distance (m)": round(segment.length_3d(), 2),
        "Total Ascent (m)": round(segment.get_uphill_downhill().uphill, 2),
        "Total Descent (m)": round(segment.get_uphill_downhill().downhill, 2),
        "Max Elevation (m)": round(max(p.elevation for p in segment.points if p.elevation), 2),
    }

    execution_time = time.perf_counter() - start_time
    results["Execution Time (s)"] = round(execution_time, 4)
    return results

def run_comparison(file_path="Test.gpx"):
    
    all_ezgpx_times = []
    all_gpxpy_times = []

    for _ in range(1):
        ezgpx_results = process_with_ezgpx(file_path)
        gpxpy_results = process_with_gpxpy(file_path)

        print("=== ezGPX Results ===")
        for k, v in ezgpx_results.items():
            if k == "Execution Time (s)":
                all_ezgpx_times.append(v)
            print(f"{k}: {v}")

        print("\n=== gpxpy Results ===")
        for k, v in gpxpy_results.items():
            if k == "Execution Time (s)":
                all_gpxpy_times.append(v)
            print(f"{k}: {v}")

        print("\n=== Comparison (ezGPX vs gpxpy) ===")
        for key in ["Total Points", "Total Distance (m)", "Total Ascent (m)", "Total Descent (m)", "Max Elevation (m)"]:
            print(f"{key}: {ezgpx_results[key]}  vs  {gpxpy_results[key]}")

    print("\n=== Comparison Summary (ezGPX vs gpxpy) ===")
    print(f'Average ezGPX Time: {sum(all_ezgpx_times) / len(all_ezgpx_times):.4f} s')
    print(f'Average gpxpy Time: {sum(all_gpxpy_times) / len(all_gpxpy_times):.4f} s')

if __name__ == "__main__":
    # run_comparison("Test1.gpx")
    # run_comparison("Test2.gpx")
    run_comparison("Test3.gpx")
