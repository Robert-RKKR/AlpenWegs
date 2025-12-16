# AlpenWegs import:
from alpenwegs.ashared.tasks.ashared.base_gpx import BaseGpxTask
from alpenwegs.logger import app_logger

# Django import:
from django.contrib.gis.geos import Point


# GPX model Task:
class GpxModelTask(
    BaseGpxTask,
):
    
    def calculate_highest_grade(self,
        segment,
    ) -> None:
        """
        Calculate the highest grade in percentage from a GPX segment.
        """
        
        highest_grade = None
        for i in range(1, len(segment.points)):
            p1 = segment.points[i - 1]
            p2 = segment.points[i]

            if p1.elevation is None or p2.elevation is None:
                continue

            distance_2d = p1.distance_2d(p2)
            if distance_2d and distance_2d > 0:
                grade = abs((p2.elevation - p1.elevation) / distance_2d) * 100
                if highest_grade is None or grade > highest_grade:
                    highest_grade = grade

        # Return highest grade rounded to 2 decimal places:
        return round(highest_grade, 2) if highest_grade is not None else None
    
    def process_and_save_gpx_data(self,
        instance,
        segment,
    ) -> None:
        """
        Process base GPX metrics data.
        """

        # Distance 3D defined latitude & longitude and elevation:
        total_distance = segment.length_3d()

        # Collect total ascent and descent:
        elevation_gain, elevation_loss = segment.get_uphill_downhill()
        average_grade = (
            elevation_gain / total_distance
        ) * 100 if total_distance else None

        # Collect all elevations to find max and min elevation:
        elevations = [
            p.elevation for p in segment.points if p.elevation is not None]
        highest_elevation = max(elevations) if elevations else None
        lowest_elevation = min(elevations) if elevations else None

        # Collect first point localization:
        first_point = segment.points[0] if segment.points else None

        if (
            first_point
            and first_point.longitude is not None
            and first_point.latitude is not None
        ):
            instance.location = Point(
                first_point.longitude,
                first_point.latitude,
                srid=4326,
            )
            instance.elevation = (
                int(first_point.elevation)
                if first_point.elevation is not None
                else None
            )
        else:
            instance.location = None
            instance.elevation = None

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
        instance.highest_elevation = self._decimal_accuracy(highest_elevation, 2)
        instance.lowest_elevation = self._decimal_accuracy(lowest_elevation, 2)
        instance.total_distance = self._decimal_accuracy(total_distance, 2)
        instance.elevation_gain = self._decimal_accuracy(elevation_gain, 2)
        instance.elevation_loss = self._decimal_accuracy(elevation_loss, 2)
        instance.average_grade = self._decimal_accuracy(average_grade, 2)
        instance.highest_grade = self.calculate_highest_grade(segment)
        instance.total_points = len(segment.points)
        instance.elevation_graph = elevation_graph
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
            'elevation',
            'location',
            'geojson',
            # 'track_types',
        ])

        # Return success value:
        return True

    def execute(self,
        instance,
    ) -> None:
        """
        Process GPX for any BaseGpxModel-based instance.
        Assumes:
        - instance.gpx_data.path is a FileField
        - instance has BaseGpxModel fields: distance, elevation_gain, etc.
        """
        
        # Collect GPX context:
        gpx_context = self.get_gpx_context(
            instance=instance,
        )

        # Check if context retrieval was successful:
        if not gpx_context:
            return False
        
        # Unpack GPX context:
        segment = gpx_context['segment']

        # Process and save GPX data to instance:
        status = self.process_and_save_gpx_data(
            instance=instance,
            segment=segment,
        )

        # Return status value:
        return status
