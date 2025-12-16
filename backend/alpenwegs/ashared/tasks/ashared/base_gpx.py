# Django import:
from django.core.files.storage import default_storage

# AlpenWegs import:
from alpenwegs.ashared.tasks.ashared.base_task import BaseTask
from alpenwegs.logger import app_logger

# Python import:
import gpxpy


class BaseGpxTask(
    BaseTask,
):
    """
    Provides parsed GPX, track and segment.
    Parsed once and cached on the instance.
    """

    def get_gpx_context(self, instance):

        # Return cached context if available:
        if hasattr(instance, "_gpx_context"):
            return instance._gpx_context

        # Collect GPX file path:
        gpx_file_field = instance.gpx_data.path
        file_path = gpx_file_field.path

        try:
            # Try to collect GPX data:
            with default_storage.open(file_path, "r") as file:
                gpx = gpxpy.parse(file)
        
        except Exception as exception:
            # Log missing file and exit:
            app_logger.error('GPX Model Task failed due to error related '
                f'with opening of gpx file. Exception: {exception}'
            )
            # Return failure value:
            return False
        
        # Check if GPX has tracks and segments:
        if not gpx.tracks or not gpx.tracks[0].segments:
            # Log missing track/segment and exit:
            app_logger.error('GPX Model Task failed due to error related '
                'with missing tracks or segments.'
            )
            # Return failure value:
            return False

        # Collect first track of the GPX:
        track = gpx.tracks[0]
        # Collect first segment of the track:
        segment = track.segments[0]

        # Check if segment has points:
        if not segment.points:
            # Log missing points and exit:
            app_logger.error('GPX Model Task failed due to error related '
                'with missing points in segment.'
            )
            # Return failure value:
            return False
        
        # Cache collected gpx data on instance:
        instance._gpx_context = {
            'track': gpx.tracks,
            'segment': segment,
            'gpx': gpx,
        }
        
        # Return collected gpx context:
        return instance._gpx_context
