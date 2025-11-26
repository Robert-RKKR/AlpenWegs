# Django import:
from django.core.files.storage import default_storage

# AlpenWegs import:
from alpenwegs.ashared.tasks.base_task import BaseTask
from alpenwegs.logger import app_logger

# Python import:
import gpxpy


# GPX model Task:
class GpxModelTask(
    BaseTask,
):
    
    # def xxx(self):
    #     highest_grade = None
    #     for i in range(1, len(segment.points)):
    #         p1 = segment.points[i - 1]
    #         p2 = segment.points[i]

    #         if p1.elevation is None or p2.elevation is None:
    #             continue

    #         distance_2d = p1.distance_2d(p2)
    #         if distance_2d and distance_2d > 0:
    #             grade = abs((p2.elevation - p1.elevation) / distance_2d) * 100
    #             if highest_grade is None or grade > highest_grade:
    #                 highest_grade = grade

    #     if highest_grade is not None:
    #         highest_grade = round(highest_grade, 2)

    def execute(self,
        instance,
    ) -> None:
        """
        Process GPX for any BaseGpxModel-based instance.
        Assumes:
        - instance.gpx_data.path is a FileField
        - instance has BaseGpxModel fields: distance, elevation_gain, etc.
        """

        # Collect GPX file path:
        gpx_file_field = instance.gpx_data.path
        file_path = gpx_file_field.path

        try:
            # Try to collect GPX data:
            with default_storage.open(file_path, "r") as file:
                gpx = gpxpy.parse(file)
        
        except Exception as exception:
            # Log missing file and exit:
            app_logger.error(f'Error processing GPX file: {exception}')
            return False
        
        # Check if GPX has tracks and segments:
        if not gpx.tracks or not gpx.tracks[0].segments:
            # Log missing track/segment and exit:
            app_logger.error('GPX track/segment missing or empty.')
            return False

        # Collect first track of the GPX:
        track = gpx.tracks[0]
        # Collect first segment of the track:
        segment = track.segments[0]

        # Check if segment has points:
        if not segment.points:
            # Log missing points and exit:
            app_logger.error('GPX segment contains no points.')
            return False

        # Distance 3D defined latitude & longitude and elevation:
        total_distance = segment.length_3d()

        # Collect total ascent and descent:
        elevation_gain, elevation_loss = segment.get_uphill_downhill()
        average_grade = (elevation_gain / total_distance) * 100 if total_distance else None

        # Collect all elevations to find max and min elevation:
        elevations = [
            p.elevation for p in segment.points if p.elevation is not None]
        highest_elevation = max(elevations) if elevations else None
        lowest_elevation = min(elevations) if elevations else None

        # Create geojson line:
        geojson = {
            'type': 'LineString',
            'coordinates': [
                [
                    point.longitude,
                    point.latitude,
                    point.elevation or 0
                ]
                for point in segment.points
            ],
        }

        # Create elevation graph data:
        elevation_graph = [
            {'index': i, 'elevation': point.elevation or 0}
            for i, point in enumerate(segment.points)
        ]

        # Update instance fields:
        instance.highest_elevation = round(highest_elevation, 2) if highest_elevation is not None else None
        instance.lowest_elevation = round(lowest_elevation, 2) if lowest_elevation is not None else None
        instance.total_distance = round(total_distance, 2) if total_distance is not None else None
        instance.elevation_gain = round(elevation_gain, 2) if elevation_gain is not None else None
        instance.elevation_loss = round(elevation_loss, 2) if elevation_loss is not None else None
        instance.average_grade = round(average_grade, 2)
        instance.total_points = len(segment.points)

        instance.elevation_graph = elevation_graph
        # instance.highest_grade = highest_grade
        # instance.track_types = track_types
        instance.geojson = geojson

        # Disable after commit to avoid recursion:
        instance._disable_after_commit = True

        # Save updated instance fields:
        instance.save(update_fields=[
            'highest_elevation',
            'lowest_elevation',
            'elevation_graph',
            'total_distance',
            'elevation_gain',
            'elevation_loss',
            'average_grade',
            'highest_grade',
            'total_points',
            'track_types',
            'geojson',
        ])


        # print("Starting GPX processing task...")
        # print(f'Instance: {instance}')

        # gpx_file_field = instance.gpx_data.path
        # file_path = gpx_file_field.path

        # with default_storage.open(file_path, "r") as f:
        #     gpx = gpxpy.parse(f)

        # track = gpx.tracks[0]
        # segment = track.segments[0]

        # # Distance
        # distance_m = segment.length_3d()
        # distance_km = distance_m / 1000

        # # Elevation
        # gain, loss = segment.get_uphill_downhill()
        # elevations = [p.elevation for p in segment.points if p.elevation is not None]

        # # Basic stats
        # instance.distance = distance_km
        # instance.elevation_gain = gain
        # instance.elevation_loss = loss
        # instance.highest_elevation = max(elevations) if elevations else None
        # instance.lowest_elevation = min(elevations) if elevations else None
        # instance.average_grade = (gain / distance_m) * 100 if distance_m else None

        # # GeoJSON line
        # instance.geojson = {
        #     "type": "LineString",
        #     "coordinates": [
        #         [p.longitude, p.latitude, p.elevation or 0]
        #         for p in segment.points
        #     ],
        # }

        # # Elevation graph
        # instance.elevation_graph = [
        #     {"idx": i, "ele": p.elevation or 0}
        #     for i, p in enumerate(segment.points)
        # ]

        # instance._disable_after_commit = True
        # instance.save(update_fields=[
        #     "total_distance",
        #     "elevation_gain",
        #     "elevation_loss",
        #     "highest_elevation",
        #     "lowest_elevation",
        #     "average_grade",
        #     "geojson",
        #     "elevation_graph",
        # ])
