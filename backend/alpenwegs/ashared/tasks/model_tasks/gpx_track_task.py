# Django import:
from django.core.files.storage import default_storage

# AlpenWegs import:
from alpenwegs.ashared.tasks.base_task import BaseTask
from alpenwegs.logger import app_logger

# Python import:
import gpxpy


# GPX model Task:
class GpxTrackModelTask(
    BaseTask,
):
    
    @staticmethod
    def _safe_timedelta_seconds(td):
        """Convert timedelta to seconds as float."""
        if td is None:
            return None
        return td.total_seconds()

    def execute(self,
        instance,
    ) -> None:
        """
        Process GPX for extended track metrics:
        - Time metrics
        - Speed metrics
        - Pace metrics
        - Moving ratios
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

        # Collect start and end times:
        start_time = segment.points[0].time
        end_time = segment.points[-1].time

        # Collect total time:
        total_time = (
            end_time - start_time
            if start_time and end_time
            else None
        )

        # Built-in GPX moving/stopped time:
        moving_time, stopped_time, moving_distance, stopped_distance, max_speed = segment.get_moving_data()

        # Convert to seconds
        moving_time_sec = moving_time
        stopped_time_sec = stopped_time
        total_time_sec = self._safe_timedelta_seconds(total_time)

        # 2. Speed values (m/s → km/h)
        def to_kmh(value_m_per_s):
            if not value_m_per_s:
                return None
            return value_m_per_s * 3.6

        average_speed = (
            moving_distance / total_time_sec if total_time_sec else None
        )
        moving_average_speed = (
            moving_distance / moving_time_sec if moving_time_sec else None
        )

        # Convert speeds to km/h
        average_speed_kmh = to_kmh(average_speed)
        moving_average_kmh = to_kmh(moving_average_speed)
        maximum_speed_kmh = to_kmh(max_speed)

        # 3. Ascent/Descent speed calculations
        elevation_gain, elevation_loss = segment.get_uphill_downhill()
        # positive descent ("loss") as absolute
        elevation_loss = abs(elevation_loss)

        ascent_time = 0.0
        descent_time = 0.0

        max_ascent_speed = 0.0
        max_descent_speed = 0.0

        for i in range(1, len(segment.points)):
            p1 = segment.points[i - 1]
            p2 = segment.points[i]

            if p1.time is None or p2.time is None:
                continue

            delta_t = (p2.time - p1.time).total_seconds()
            if delta_t <= 0:
                continue

            delta_h = (p2.elevation - p1.elevation) if (p1.elevation is not None and p2.elevation is not None) else 0

            speed_m_s = abs(delta_h) / delta_t if delta_t else 0
            speed_km_h = speed_m_s * 3.6

            # Ascent
            if delta_h > 0:
                ascent_time += delta_t
                if speed_km_h > max_ascent_speed:
                    max_ascent_speed = speed_km_h

            # Descent
            if delta_h < 0:
                descent_time += delta_t
                if speed_km_h > max_descent_speed:
                    max_descent_speed = speed_km_h

        ascent_average_speed = (
            (elevation_gain / ascent_time) * 3.6 if ascent_time > 0 else None
        )
        descent_average_speed = (
            (elevation_loss / descent_time) * 3.6 if descent_time > 0 else None
        )

        # 4. Pace calculations (min/km)
        total_distance = segment.length_3d()

        def to_pace(distance_m, time_seconds):
            """Return pace as min/km."""
            if not distance_m or not time_seconds:
                return None
            pace_sec_per_km = time_seconds / (distance_m / 1000)
            return pace_sec_per_km / 60.0  # minutes/km

        pace_average = to_pace(total_distance, total_time_sec)
        pace_best = to_pace(moving_distance, moving_time_sec)

        # 5. Moving ratio
        moving_ratio = (
            moving_time_sec / total_time_sec if total_time_sec else None
        )

        # Write into model instance
        instance.start_time = start_time
        instance.end_time = end_time
        instance.duration = total_time_sec
        instance.moving_time = moving_time_sec
        instance.total_time = total_time_sec
        instance.stop_time = stopped_time_sec

        instance.average_speed = round(average_speed_kmh, 2) if average_speed_kmh else None
        instance.moving_average_speed = round(moving_average_kmh, 2) if moving_average_kmh else None
        instance.maximum_speed = round(maximum_speed_kmh, 2) if maximum_speed_kmh else None

        instance.ascent_average_speed = round(ascent_average_speed, 2) if ascent_average_speed else None
        instance.descent_average_speed = round(descent_average_speed, 2) if descent_average_speed else None
        instance.maximum_ascent_speed = round(max_ascent_speed, 2) if max_ascent_speed else None
        instance.maximum_descent_speed = round(max_descent_speed, 2) if max_descent_speed else None

        instance.moving_ratio = round(moving_ratio, 4) if moving_ratio else None
        instance.pace_average = round(pace_average, 3) if pace_average else None
        instance.pace_best = round(pace_best, 3) if pace_best else None

        # Disable after-commit hooks
        instance._disable_after_commit = True

        instance.save(update_fields=[
            'start_time',
            'end_time',
            'duration',
            'moving_time',
            'total_time',
            'stop_time',
            'average_speed',
            'moving_average_speed',
            'ascent_average_speed',
            'descent_average_speed',
            'maximum_speed',
            'maximum_ascent_speed',
            'maximum_descent_speed',
            'moving_ratio',
            'pace_average',
            'pace_best',
        ])

        # Return success value:
        return True
