# AlpenWegs import:
from alpenwegs.ashared.models.relationship_model import BaseRelationshipOrderedModel
from alpenwegs.ashared.constants.section_poi_category import SectionPoiRoleChoices
from alpenwegs.ashared.models.characteristic_model import BaseCharacteristicModel
from alpenwegs.ashared.models.identification_model import BaseIdentificationModel
from alpenwegs.ashared.models.sport_category_model import BaseSportCategoryModel
from alpenwegs.ashared.models.relationship_model import BaseRelationshipModel
from alpenwegs.ashared.models.descriptive_model import BaseDescriptiveModel
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel
from alpenwegs.ashared.models.creator_model import BaseCreatorModel
from alpenwegs.ashared.models.liked_model import BaseLikedModel
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
    BaseCharacteristicModel,
    BaseIdentificationModel,
    BaseSportCategoryModel,
    BaseDescriptiveModel,
    BaseTimestampModel,
    BaseCreatorModel,
    BaseLikedModel,
    BaseGpxModel,
):
    """
    Model representing single route Section.
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


# Section Model Many-to-many relationships with other models:
class SectionToPoiModel(
    BaseRelationshipOrderedModel,
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
    role = models.IntegerField(
        choices=SectionPoiRoleChoices.choices,
        db_index=True,
        verbose_name='Role',
        help_text=(
            'Role of this Point of Interest within the section’s path. "START" '
            'marks the logical beginning of the section (at most one per '
            'section). "VIA" intermediate waypoint(s) along the section; '
            'multiple allowed and ordered via seq_index; annotations that do '
            'not change the section geometry. "END" marks the logical end of '
            'the section (at most one per section). The POI does not have to '
            'lie exactly on the path; nearby POIs may be snapped to the line '
            'or connected visually. Typical anchors: START ≈ 0 m, END ≈ total '
            'length.'
        ),
        default=SectionPoiRoleChoices.VIA,
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
