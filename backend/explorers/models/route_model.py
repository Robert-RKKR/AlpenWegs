# AlpenWegs import:
from alpenwegs.ashared.models.characteristic_model import BaseCharacteristicModel
from alpenwegs.ashared.models.identification_model import BaseIdentificationModel
from alpenwegs.ashared.models.sport_category_model import BaseSportCategoryModel
from alpenwegs.ashared.models.accomplished_model import BaseAccomplishedModel
from alpenwegs.ashared.models.descriptive_model import BaseDescriptiveModel
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel
from alpenwegs.ashared.models.statistic_model import BaseStatisticModel
from alpenwegs.ashared.models.creator_model import BaseCreatorModel
from alpenwegs.ashared.models.liked_model import BaseLikedModel
from alpenwegs.ashared.models.score_model import BaseScoreModel

# Django import:
from django.db import models


# Route Model class:
class RouteModel(
    BaseCharacteristicModel,
    BaseIdentificationModel,
    BaseSportCategoryModel,
    BaseAccomplishedModel,
    BaseDescriptiveModel,
    BaseTimestampModel,
    BaseStatisticModel,
    BaseCreatorModel,
    BaseLikedModel,
    BaseScoreModel,
):
    """
    Model representing single Route.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'

    # Route Many-to-Many Relationships:
    trips = models.ManyToManyField(
        'TripModel',
        through='TripToRouteModel',
        related_name='route_trips',
        verbose_name='Route Trips',
        help_text='Trips that include this route '
            'as part of a multi-day experience.'
    )
