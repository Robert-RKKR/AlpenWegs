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
from compendiums.models.poi_model import PoiModel
from assets.models.photo_model import PhotoModel

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
    Represents a single route section within the AlpenWegs system.

    A section is the core building block of a route. It combines 
    geographical, descriptive, and sport-specific characteristics 
    (difficulty, sport category, GPX geometry, etc.) and links to 
    related Points of Interest, Cards, and Regions.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

        # Add custom AlpenWegs permissions:
        permissions = [
            ('change_own_sectionmodel', 'Can change own sections'),
            ('change_all_sectionmodel', 'Can change all sections'),
            ('delete_own_sectionmodel', 'Can delete own sections'),
            ('delete_all_sectionmodel', 'Can delete all sections'),
            ('view_own_sectionmodel', 'Can view own sections'),
            ('view_all_sectionmodel', 'Can view all sections'),
            ('add_own_sectionmodel', 'Can add own sections'),
        ]

    # Default roles and their permissions:
    ROLE_PERMS = {
        'Member': [
            'change_own',
            'delete_own',
            'view_own',
            'add_own'
        ],
        'Author': [
            'change_own',
            'delete_own',
            'view_own',
            'add_own'
        ],
        'Admin':  [
            'change_all',
            'change_own',
            'delete_all',
            'delete_own',
            'view_all',
            'view_own',
            'add_own',
        ],
    }

    # Section Many-to-Many Relationships:
    photos = models.ManyToManyField(
        PhotoModel,
        through='SectionToPhotoModel',
        related_name='section_photos',
        verbose_name='Section Photos',
        help_text='A collection of photos that are linked to '
            'the section and that provide a visual documentation '
            'of the section created by the section creator.'
    )
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
        help_text='Geographical regions that this section crosses '
            'or belongs to. Useful for filtering and categorization.'
    )

    # Section Many-to-Many Relationships (reverse side):
    routes = models.ManyToManyField(
        'RouteModel',
        through='SectionToRouteModel',
        related_name='route_sections',
        verbose_name='Route Sections',
        help_text='Sections that are part of this route.'
    )


class SectionToPhotoModel(
    BaseRelationshipModel,
):
    """
    Intermediate model linking a Section to Photos.

    Stores the association between a route section and one or more 
    photos that visually document the section. This enables attaching 
    user-contributed or system-provided media to enhance the section’s 
    descriptive context.
    """
    
    # Base relation between Many-to-many Models:
    section = models.ForeignKey(
        SectionModel,
        related_name='photo_section_associations',
        verbose_name='Section',
        help_text='The Section that is associated with the Photo '
            'to Section M2M relationship.',
        on_delete=models.PROTECT,
    )
    photo = models.ForeignKey(
        PhotoModel,
        related_name='section_photo_associations',
        verbose_name='Photo',
        help_text='The Photo that is associated with the Section '
            'to Photo M2M relationship.',
        on_delete=models.PROTECT,
    )


# Section Model Many-to-many relationships with other models:
class SectionToPoiModel(
    BaseRelationshipOrderedModel,
):
    """
    Intermediate model linking a Section to one or more
    Points of Interest (PoIs).

    Stores the ordered association and semantic role of a PoI
    within the section's path. For example, a PoI can mark the
    start, an intermediate waypoint, or the end of the section.
    """
    
    # Base relation between Many-to-many Models:
    section = models.ForeignKey(
        SectionModel,
        related_name='poi_section_associations',
        verbose_name='Section',
        help_text='The Section that is associated with the Point of '
            'Interest to Section M2M relationship.',
        on_delete=models.PROTECT,
    )
    poi = models.ForeignKey(
        PoiModel,
        related_name='section_poi_associations',
        verbose_name='Point of Interest',
        help_text='The Point of Interest that is associated with the '
            'Section to Point of Interest M2M relationship.',
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


class SectionToCardModel(
    BaseRelationshipModel,
):
    """
    Intermediate model linking a Section to Cards.

    Allows tracking which achievement sections are tied to 
    completing this section.
    """
    
    # Base relation between Many-to-many Models:
    section = models.ForeignKey(
        SectionModel,
        related_name='card_section_associations',
        verbose_name='Section',
        help_text='The Section that is associated with the Card '
            'to Section M2M relationship.',
        on_delete=models.PROTECT,
    )
    card = models.ForeignKey(
        CardModel,
        related_name='section_card_associations',
        verbose_name='Card',
        help_text='The Card that is associated with the Section '
            'to Card M2M relationship.',
        on_delete=models.PROTECT,
    )


class SectionToRegionModel(
    BaseRelationshipModel,
):
    """
    Intermediate model linking a Section to Regions.

    Represents the geographical regions that a section belongs to 
    or traverses, enabling filtering and classification.
    """
    
    # Base relation between Many-to-many Models:
    section = models.ForeignKey(
        SectionModel,
        related_name='region_section_associations',
        verbose_name='Section',
        help_text='The Section that is associated with the Region '
            'to Section M2M relationship.',
        on_delete=models.PROTECT,
    )
    region = models.ForeignKey(
        RegionModel,
        related_name='section_region_associations',
        verbose_name='Region',
        help_text='The Region that is associated with the Section '
            'to Region M2M relationship.',
        on_delete=models.PROTECT,
    )
