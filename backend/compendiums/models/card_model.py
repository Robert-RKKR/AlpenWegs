# AlpenWegs import:
from alpenwegs.ashared.constants.sport_category_difficulty import SportCategoryDifficultyChoices
from alpenwegs.ashared.models.identification_model import BaseIdentificationModel
from alpenwegs.ashared.constants.sport_category import SportCategoryChoices
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel
from alpenwegs.ashared.models.creator_model import BaseCreatorModel
from alpenwegs.ashared.constants.card_type import CardTypeChoices

# AlpenWegs application import:
from compendiums.models.poi_model import PoiModel

# Django import:
from django.db import models


# Card Model class:
class CardModel(
    BaseIdentificationModel,
    BaseTimestampModel,
    BaseCreatorModel,
):
    """
    Country Model for storing details about a country.
    """

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

    # Default roles and their permissions:
    ROLE_PERMS = {
        'Member': ['view'],
        'Author': ['view', 'add', 'change', 'delete'],
        'Admin':  ['view', 'add', 'change', 'delete'],
    }
    
    # Card Many-to-many relationships:
    # routes = models.ManyToManyField(
    #     'routes.RouteModel',
    #     through='routes.RouteToCardModel',
    #     related_name='card_routes',
    #     verbose_name='Associated Routes.',
    # )
    # users = models.ManyToManyField(
    #     'profiles.UserModel',
    #     through='profiles.UserToCardModel',
    #     related_name='card_users',
    #     verbose_name='Users',
    #     help_text='Associated Users.',
    # )

    # Card One-to-One relationships:
    poi = models.ForeignKey(
        PoiModel,
        verbose_name='Point of Interest',
        help_text='Associated Point of Interest.',
        on_delete=models.PROTECT,
    )

    # Card specific values:
    description = models.TextField(
        verbose_name='Card Description',
        help_text='Main text shown on the card (summary, '
            'story, or important information).',
    )
    elevation = models.FloatField(
        verbose_name='Elevation (m a.s.l.)',
        help_text='Approximate elevation (in meters above '
            'sea level) where the card’s feature is located.',
    )
    type = models.CharField(
        choices=CardTypeChoices.choices,
        verbose_name='Card Type',
        help_text='Specifies the type of feature this card '
            'represents (e.g., mountain peak, hut, lake).',
        max_length=32,
        default=CardTypeChoices.MOUNTAIN_PEAK,
    )
    category = models.IntegerField(
        choices=SportCategoryChoices.choices,
        verbose_name='Sport Category',
        help_text='The sport or activity associated with this '
            'card (e.g., hiking, via ferrata, climbing, biking).',
        default=SportCategoryChoices.HIKING,
    )
    category_specific_difficulty = models.IntegerField(
        choices=SportCategoryDifficultyChoices.choices,
        verbose_name='Difficulty Level',
        help_text='Difficulty level within the chosen sport category '
            '(e.g., T2 for hiking, K3 for via ferrata). Optional field.',
        default=SportCategoryDifficultyChoices.T3,
    )
