# Django import:
from django.core.files.storage import default_storage

# AlpenWegs import:
from alpenwegs.ashared.tasks.base_task import BaseTask

# Python import:
import gpxpy


# GPX model Task:
class GpxModelTask(
    BaseTask,
):

    def execute(self,
        instance,
    ) -> None:
        """
        Process GPX for any BaseGpxModel-based instance.
        Assumes:
        - instance.gpx_data.path is a FileField
        - instance has BaseGpxModel fields: distance, elevation_gain, etc.
        """

        print("Starting GPX processing task...")
        print(f'Instance: {instance}')

        gpx_file_field = instance.gpx_data.path
        file_path = gpx_file_field.path

        with default_storage.open(file_path, "r") as f:
            gpx = gpxpy.parse(f)

        track = gpx.tracks[0]
        segment = track.segments[0]

        # Distance
        distance_m = segment.length_3d()
        distance_km = distance_m / 1000

        # Elevation
        gain, loss = segment.get_uphill_downhill()
        elevations = [p.elevation for p in segment.points if p.elevation is not None]

        # Basic stats
        instance.distance = distance_km
        instance.elevation_gain = gain
        instance.elevation_loss = loss
        instance.highest_elevation = max(elevations) if elevations else None
        instance.lowest_elevation = min(elevations) if elevations else None
        instance.average_grade = (gain / distance_m) * 100 if distance_m else None

        # GeoJSON line
        instance.geojson = {
            "type": "LineString",
            "coordinates": [
                [p.longitude, p.latitude, p.elevation or 0]
                for p in segment.points
            ],
        }

        # Elevation graph
        instance.elevation_graph = [
            {"idx": i, "ele": p.elevation or 0}
            for i, p in enumerate(segment.points)
        ]

        instance._disable_after_commit = True
        instance.save(update_fields=[
            "total_distance",
            "elevation_gain",
            "elevation_loss",
            "highest_elevation",
            "lowest_elevation",
            "average_grade",
            "geojson",
            "elevation_graph",
        ])
