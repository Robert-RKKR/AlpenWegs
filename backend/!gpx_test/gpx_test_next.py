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

    track = gpx.tracks[0]
    segment = track.segments[0]

    # ----------------------------
    # Base distance calculations
    # ----------------------------
    distance_3d = segment.length_3d()
    distance_2d = segment.length_2d()

    total_ascent, total_descent = segment.get_uphill_downhill()

    elevations = [p.elevation for p in segment.points if p.elevation]
    max_ele = max(elevations) if elevations else None
    min_ele = min(elevations) if elevations else None

    (
        moving_time,
        stopped_time,
        moving_distance,
        stopped_distance,
        max_speed
    ) = segment.get_moving_data()

    # ----------------------------
    # Core computed metrics
    # ----------------------------
    avg_speed_overall = (
        distance_3d / (moving_time + stopped_time)
        if (moving_time + stopped_time) > 0 else 0
    )

    avg_speed_moving = (
        moving_distance / moving_time
        if moving_time > 0 else 0
    )

    # ascent speed (m/h)
    ascent_speed = (
        total_ascent / (moving_time / 3600)
        if moving_time > 0 else 0
    )

    # ----------------------------
    # NEW METRICS YOU REQUESTED
    # ----------------------------

    # total time in sec
    total_time = moving_time + stopped_time

    # average grade %
    average_grade = (
        (total_ascent / distance_3d) * 100
        if distance_3d > 0 else 0
    )

    # highest grade (point to point)
    highest_grade = 0
    for i in range(len(segment.points) - 1):
        p1 = segment.points[i]
        p2 = segment.points[i + 1]
        if p1.elevation and p2.elevation:
            d = p1.distance_3d(p2)
            if d > 0:
                g = ((p2.elevation - p1.elevation) / d) * 100
                if g > highest_grade:
                    highest_grade = g

    # elevation graph every point (simplest)
    elevation_graph = [
        [i, p.elevation] for i, p in enumerate(segment.points)
        if p.elevation
    ]

    # ascent speed average km/h
    ascent_average_speed = (
        ascent_speed / 1000 * 1
    )

    # descent section average speed
    descent_average_speed = (
        total_descent / (moving_time / 3600)
        if moving_time > 0 else 0
    )

    # maximum ascent speed (rough)
    maximum_ascent_speed = ascent_speed

    # maximum descent speed rough
    maximum_descent_speed = descent_average_speed

    # moving average speed in km/h
    moving_average_speed = avg_speed_moving * 3.6

    # moving ratio %
    moving_ratio = (
        moving_time / total_time * 100
        if total_time > 0 else 0
    )

    # pace average min per km
    pace_average = (
        (moving_time / 60) / (distance_3d / 1000)
        if distance_3d > 0 else 0
    )

    pace_best = pace_average  # placeholder


    # ----------------------------
    # PRINT RESULTS
    # ----------------------------
    print("=== GPX Stats with gpxpy ===")
    print(f"Track name: {track.name}")
    print(f"Points count: {len(segment.points)}")
    print(f"Distance 3d: {distance_3d:.2f}")
    print(f"Total ascent: {total_ascent:.2f}")
    print(f"Total descent: {total_descent:.2f}")
    print(f"Max elevation: {max_ele}")
    print(f"Min elevation: {min_ele}")
    print()

    # NEW
    print(f"Average grade: {average_grade:.2f}")
    print(f"Highest grade: {highest_grade:.2f}")
    print(f"Elevation graph points: {len(elevation_graph)}")
    print()

    print(f"Total time: {total_time:.2f}")
    print(f"Ascent avg speed: {ascent_average_speed:.2f}")
    print(f"Descent avg speed: {descent_average_speed:.2f}")
    print(f"Max ascent speed: {maximum_ascent_speed:.2f}")
    print(f"Max descent speed: {maximum_descent_speed:.2f}")
    print(f"Moving avg speed: {moving_average_speed:.2f}")
    print(f"Moving ratio: {moving_ratio:.2f}")
    print(f"Pace avg: {pace_average:.2f}")
    print(f"Pace best: {pace_best:.2f}")
    print()


# test
process_gpx("gpx/AAA.gpx")
