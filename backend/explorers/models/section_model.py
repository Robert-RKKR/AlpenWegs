# AlpenWegs import:
from alpenwegs.ashared.constants.sport_category_difficulty import SportCategoryDifficultyChoices
from alpenwegs.ashared.models.identification_model import BaseIdentificationModel
from alpenwegs.ashared.models.relationship_model import BaseRelationshipModel
from alpenwegs.ashared.constants.sport_category import SportCategoryChoices
from alpenwegs.ashared.models.descriptive_model import BaseDescriptiveModel
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel
from alpenwegs.ashared.models.statistic_model import BaseStatisticModel
from alpenwegs.ashared.models.creator_model import BaseCreatorModel
from alpenwegs.ashared.models.score_model import BaseScoreModel
from alpenwegs.ashared.models.gpx_model import BaseGpxModel

# AlpenWegs application import:
from compendiums.models.region_model import RegionModel
from compendiums.models.card_model import CardModel
# from assets.models.photo_model import PhotoModel
from compendiums.models.poi_model import PoiModel

# Django import:
from django.db import models


# Section Model class:
class SectionModel(
    BaseIdentificationModel,
    BaseDescriptiveModel,
    BaseTimestampModel,
    BaseStatisticModel,
    BaseCreatorModel,
    BaseScoreModel,
    BaseGpxModel,
):
    """
    Model representing section sections.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

    # Many-to-Many Relationships:
    # photos = models.ManyToManyField(
    #     PhotoModel,
    #     through='SectionToPhotoModel',
    #     related_name='section_photos',
    #     verbose_name='Section Photos',
    #     help_text='A collection of photos that are linked to '
    #         'the section and that provide a visual documentation '
    #         'of the section created by the section creator.'
    # )
    pois = models.ManyToManyField(
        PoiModel,
        through='SectionToPoiModel',
        related_name='section_pois',
        verbose_name='Section Points of Interest (PoIs)',
        help_text='A list of Points of Interest associated '
            'with the section, highlighting key places for travelers '
            'to visit along the way. Points of Interest also '
            'mark the start and end points of the section.'
    )
    cards = models.ManyToManyField(
        CardModel,
        through='SectionToCardModel',
        related_name='section_cards',
        verbose_name='Section Cards',
        help_text='Cards associated with the section that can '
            'be obtained by the user by completing this section.'
    )
    regions = models.ManyToManyField(
        RegionModel,
        through='SectionToRegionModel',
        related_name='section_regions',
        verbose_name='Section Regions',
        help_text='Geographical regions through which the '
            'section passes.'
    )

    # Category value:
    category = models.IntegerField(
        choices=SportCategoryChoices.choices,
        verbose_name='Sport Category',
        help_text='The sport or activity associated with this '
            'section (e.g., hiking, via ferrata, climbing, biking).',
        default=SportCategoryChoices.HIKING,
    )

    # Level characteristics values:
    difficulty = models.CharField(
        verbose_name='General Difficulty Level',
        help_text='Overall difficulty level of the section. Options '
            'include: Easy, Moderate, Difficult, Very Difficult, '
            'and Extremely Difficult sections.',
        max_length=32,
        blank=True,
        null=True,
    )
    category_specific_difficulty = models.IntegerField(
        choices=SportCategoryDifficultyChoices.choices,
        verbose_name='Difficulty Level',
        help_text='Difficulty level within the chosen sport category '
            '(e.g., T2 for hiking, K3 for via ferrata). Optional field.',
        default=SportCategoryDifficultyChoices.T3,
    )
    stamina_requirement = models.CharField(
        verbose_name='Stamina Requirement',
        help_text='Level of stamina required to complete the section.',
        max_length=32,
        blank=True,
        null=True,
    )
    experience_requirement = models.CharField(
        verbose_name='Experience Requirement',
        help_text='Level of experience required to safely '
            'complete the entire section.',
        max_length=32,
        blank=True,
        null=True,
    )
    potential_risk_requirement = models.CharField(
        verbose_name='Risk Requirement',
        help_text='Potential risks associated with this section.',
        max_length=32,
        blank=True,
        null=True,
    )
    potential_risk_description = models.CharField(
        verbose_name='Risk Description',
        help_text='Detailed description of possible hazards along the section.',
        max_length=1024,
        blank=True,
        null=True,
    )

    # Seasonal Information:
    best_seasons = models.CharField(
        verbose_name='Best Seasons',
        help_text='Best seasons for hiking this section.',
        max_length=32,
        blank=True,
        null=True,
    )
    best_months = models.JSONField(
        verbose_name='Best Months',
        help_text='List of best months to complete this section.',
        blank=True,
        null=True,
    )
    winter_season = models.BooleanField(
        verbose_name='Available in Winter',
        help_text='Indicates if the section is accessible in winter.',
        blank=True,
        null=True,
    )
    summer_season = models.BooleanField(
        verbose_name='Available in Summer',
        help_text='Indicates if the section is accessible in summer.',
        blank=True,
        null=True,
    )
    family_friendly = models.BooleanField(
        verbose_name='Family Friendly',
        help_text='Indicates if the section is suitable for families.',
        blank=True,
        null=True,
    )

    # API-Related Fields
    photo_primary = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    user_difficulty = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    user_duration = models.BigIntegerField(
        blank=True,
        null=True,
    )


# Section Model Many-to-many relationships with other models:
class SectionToPoiModel(
    BaseRelationshipModel,
):
    """
    An intermediate model for associating a Point of Interest
    (PoI) with a section. This model allows us to store the
    relationship between a PoI and a specific section.
    """
    
    # Base relation between Many-to-many Models:
    section = models.ForeignKey(
        SectionModel,
        related_name='poi_section_associations',
        verbose_name='Section',
        help_text='The section that this point of interest is associated with.',
        on_delete=models.PROTECT,
    )
    poi = models.ForeignKey(
        PoiModel,
        related_name='section_poi_associations',
        verbose_name='Point of Interest',
        help_text='The point of interest associated with a section.',
        on_delete=models.PROTECT,
    )
    
    # PoI role in relation to section:
    start_point = models.BooleanField(
        default=False,
        verbose_name='Is Start Point',
        help_text='Indicates whether this point of interest is the '
            'starting point of the associated section. If True, this PoI '
            'marks the beginning of the section; otherwise, it is other '
            'typ of associated PoI like end or middle point.',
    )
    end_point = models.BooleanField(
        default=False,
        verbose_name='Is End Point',
        help_text='Indicates whether this point of interest is the '
            'ending point of the associated section. If True, this PoI '
            'marks the end of the section; otherwise, it is other '
            'typ of associated PoI like beginning or middle point.',
    )
    middle_point = models.BooleanField(
        default=False,
        verbose_name='Is Middle Point',
        help_text='Indicates whether this point of interest is the '
            'middle point of the associated section. If True, this PoI '
            'is considered as a middle or intermediate point along '
            'the section; otherwise, it is other typ of associated '
            'PoI like beginning or end point of the section.',
    )


# class SectionToPhotoModel(
#     BaseRelationshipModel,
# ):
#     """
#     An intermediate model for associating a Photo
#     with a section. This model allows us to store the
#     relationship between a Photo and a specific section.
#     """
    
#     # Base relation between Many-to-many Models:
#     section = models.ForeignKey(
#         SectionModel,
#         related_name='photo_section_associations',
#         verbose_name='Section',
#         help_text='The section that this point of interest is associated with.',
#         on_delete=models.PROTECT,
#     )
#     photo = models.ForeignKey(
#         PhotoModel,
#         related_name='section_photo_associations',
#         verbose_name='Photo',
#         help_text='Xxx.',
#         on_delete=models.PROTECT,
#     )


class SectionToCardModel(
    BaseRelationshipModel,
):
    """
    An intermediate model for associating a card
    with a section. This model allows us to store the
    relationship between a Card and a specific section.
    """
    
    # Base relation between Many-to-many Models:
    section = models.ForeignKey(
        SectionModel,
        related_name='card_section_associations',
        verbose_name='Section',
        help_text='The section that this point of interest is associated with.',
        on_delete=models.PROTECT,
    )
    card = models.ForeignKey(
        CardModel,
        related_name='section_card_associations',
        verbose_name='Card',
        help_text='Xxx.',
        on_delete=models.PROTECT,
    )


class SectionToRegionModel(
    BaseRelationshipModel,
):
    """
    An intermediate model for associating a region
    with a section. This model allows us to store the
    relationship between a Card and a specific section.
    """
    
    # Base relation between Many-to-many Models:
    section = models.ForeignKey(
        SectionModel,
        related_name='region_section_associations',
        verbose_name='Section',
        help_text='The section that this point of interest is associated with.',
        on_delete=models.PROTECT,
    )
    region = models.ForeignKey(
        RegionModel,
        related_name='section_region_associations',
        verbose_name='Region',
        help_text='Xxx.',
        on_delete=models.PROTECT,
    )
