import gpxpy
import gpxpy.gpx

points = [
    ['2.681679', '1.225483', 'zug station'],
    ['2.681695', '1.225735', 'Zug'],
    ['2.683766', '1.223240', 'Zugerberg'],
    ['2.686765', '1.221233', 'unterägeri'],
    ['2.690775', '1.215215', 'sattel'],
]


def process_gpx(file_path="Test4.gpx"):

    with open(file_path, "r") as f:
        gpx = gpxpy.parse(f)

    # Track define a single activity (e.g., a run, a bike ride, etc.):
    track = gpx.tracks[0]
    # Segment define a continuous part of a track (e.g., between pauses):
    segment = track.segments[0]

    # Distance 3D defined latitude & longitude and elevation:
    distance_3d = segment.length_3d()

    # Distance 2D defined latitude & longitude only:
    distance_2d = segment.length_2d()

    # Collect total ascent and descent:
    total_ascent, total_descent = segment.get_uphill_downhill()

    # Collect all elevations to find max and min elevation:
    elevations = [p.elevation for p in segment.points if p.elevation is not None]
    max_ele = max(elevations) if elevations else None
    min_ele = min(elevations) if elevations else None

    # Collect moving data:
    moving_time, stopped_time, moving_distance, stopped_distance, max_speed = segment.get_moving_data()

    # Average speeds
    avg_speed_overall = distance_3d / (moving_time + stopped_time) if (moving_time + stopped_time) > 0 else 0
    avg_speed_moving = moving_distance / moving_time if moving_time > 0 else 0

    # --- Ascent speed (vertical meters per hour) ---
    ascent_speed = (total_ascent / (moving_time / 3600)) if moving_time > 0 else 0

    # --- Print results ---
    print("=== GPX Stats with gpxpy ===")
    print(f"Track name: {track.name}")#
    print(f"Total points: {len(segment.points)}")#
    print(f"Total distance: {distance_3d:.2f} m")#
    print(f"Total ascent: {total_ascent:.2f} m")#
    print(f"Total descent: {total_descent:.2f} m")#
    print(f"Max elevation: {max_ele:.2f} m")#
    print(f"Min elevation: {min_ele:.2f} m")#
    
    print(f"Overall avg speed: {avg_speed_overall:.2f} m/s ({avg_speed_overall*3.6:.2f} km/h)")#
    print(f"Moving avg speed: {avg_speed_moving:.2f} m/s ({avg_speed_moving*3.6:.2f} km/h)")#
    print(f"Max speed: {max_speed:.2f} m/s ({max_speed*3.6:.2f} km/h)")#
    print(f"Ascent speed: {ascent_speed:.2f} m/h")#
    print(f"Moving time: {moving_time/60:.2f} min")#
    print(f"Stopped time: {stopped_time/60:.2f} min")#
    print(f"Stopped distance: {stopped_distance/60:.2f} m")#

    """
    average_grade
    highest_grade
    elevation_graph
    total_time
    ascent_average_speed
    descent_average_speed
    maximum_ascent_speed
    maximum_descent_speed
    moving_average_speed
    moving_ratio
    pace_average
    pace_best
    """



print("\nAAA.gpx")
process_gpx("gpx/AAA.gpx")
# # Run on your GPX file
# print("\nProcessing Serqueaux_Dieppe.gpx")
# process_gpx("gpx/Serqueaux_Dieppe.gpx")
# print("\nProcessing Southampton_Portsmouth.gpx")
# process_gpx("gpx/Southampton_Portsmouth.gpx")
# print("\nProcessing Vitry-le-Francois_Langres.gpx")
# process_gpx("gpx/Vitry-le-Francois_Langres.gpx")
# print("\nProcessing VoieVerteHauteVosges.gpx")
# process_gpx("gpx/VoieVerteHauteVosges.gpx")
