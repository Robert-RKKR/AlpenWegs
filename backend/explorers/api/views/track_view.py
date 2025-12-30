# AlpenWegs application import:
from explorers.api.serializers.track_serializer import TrackRepresentationSerializer
from explorers.api.serializers.track_serializer import TrackDetailedSerializer
from explorers.api.serializers.track_serializer import TrackRelationSerializer
from explorers.models.track_model import TrackToPhotoModel
from explorers.api.filters.track_filter import TrackFilter
from explorers.models.track_model import TrackModel
from assets.models.photo_model import PhotoModel

# AlpenWegs import:
from alpenwegs.ashared.api.schemas.schema_full_generator import red_write_schema
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from alpenwegs.ashared.api.base_exceptions import ValidationAPIException
from alpenwegs.ashared.api.base_model_viewset import ReadWriteViewSet

# API import:
from drf_spectacular.utils import extend_schema_view
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_framework import status
from django.shortcuts import get_object_or_404


# Track Model API view class:
@extend_schema_view(
    **red_write_schema(
        representation_schema=TrackRepresentationSerializer,
        detailed_schema=TrackDetailedSerializer,
        relation_schema=TrackRelationSerializer,
        application_repr='Explorers',
        object_repr='Track',
    )
)
class TrackView(
    ReadWriteViewSet,
):
    """
    Read-write API view for the Track model.
    """

    # Create change notifications:
    send_notification = False
    create_change = True

    # Queryset for the view (Legacy, required by DRF):
    queryset = TrackModel.objects.all()

    # Model and query ordering used for the view:
    query_ordering = '-created'
    query_model = TrackModel

    # Serializer class (Legacy, required by DRF):
    serializer_class = TrackDetailedSerializer

    # Serializer class used for the view:
    representation_serializer_class = TrackRepresentationSerializer
    detailed_serializer_class = TrackDetailedSerializer
    relation_serializer_class = TrackRelationSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = TrackFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'

    @action(detail=True, methods=['post'], url_path='photos-relations')
    def photos_relations(
        self,
        request,
        pk=None,
    ):
        """
        Replace all existing Track–Photo relations.

        Existing relations are removed and replaced with a new set of
        relations based on provided photo UUIDs. One photo may be marked
        as the primary Track photo.
        """

        # Get the current Track object
        track_object = self.get_object()

        # Read request payload
        photo_primary = request.data.get('photo_primary', None)
        photo_ids = request.data.get('photo_ids')

        # Validate photo_ids
        if not isinstance(photo_ids, list) or not all(isinstance(p, str) for p in photo_ids):
            raise ValidationAPIException(
                error_message=(
                    'The photo_ids field must be provided and must be a list '
                    'of photo UUID strings.'
                ),
                error_details=None,
            )

        # Validate photo_primary
        if photo_primary is not None and not isinstance(photo_primary, str):
            raise ValidationAPIException(
                error_message=(
                    'The photo_primary field must be a UUID string when provided.'
                ),
                error_details=None,
            )

        # Ensure primary photo belongs to the provided photo list
        if photo_primary and photo_primary not in photo_ids:
            raise ValidationAPIException(
                error_message=(
                    'The photo_primary UUID must be included in the photo_ids list.'
                ),
                error_details=None,
            )

        # Fetch and validate Photo objects
        photos = PhotoModel.objects.filter(pk__in=photo_ids)

        if photos.count() != len(photo_ids):
            raise ValidationAPIException(
                error_message=(
                    'One or more provided photo_ids do not correspond to '
                    'existing Photo objects.'
                ),
                error_details=None,
            )

        # Build lookup map for deterministic relation creation
        photo_map = {
            str(photo.pk): photo
            for photo in photos
        }

        # Remove existing Track–Photo relations
        track_object.photo_track_associations.all().delete()

        # Create new Track–Photo relations
        relations = []
        for photo_id in photo_ids:
            relations.append(
                TrackToPhotoModel(
                    track=track_object,
                    photo=photo_map[photo_id],
                    is_primary=(photo_id == photo_primary),
                )
            )

        TrackToPhotoModel.objects.bulk_create(relations)

        # Return response
        return Response(
            {
                'track': str(track_object.pk),
                'photo_primary': photo_primary,
                'photo_relations': [
                    {
                        'photo': str(relation.photo.pk),
                        'is_primary': relation.is_primary,
                    }
                    for relation in relations
                ],
            },
            status=status.HTTP_200_OK,
        )
