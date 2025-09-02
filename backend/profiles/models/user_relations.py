# AlpenWegs import:
from alpenwegs.ashared.models.relationship_model import BaseRelationshipModel


# AlpenWegs application import:
from explorers.models.section_model import SectionModel
from compendiums.models.card_model import CardModel
from profiles.models.user_model import UserModel

# Django import:
from django.db import models


# Other User Many-to-Many Relationships Models:
class UserToCardModel(BaseRelationshipModel):
    """
    Represents a many-to-many relationship between users and cards
    they have earned or collected. This model tracks which users
    have received or are associated with specific card.
    """

    class Meta:

        # Model name values:
        verbose_name = 'User to Card'
        verbose_name_plural = 'Users to Cards'
    
    # Base relation between Many-to-many Models:
    user = models.ForeignKey(
        UserModel,
        related_name='card_user_associations',
        verbose_name='User',
        help_text='The user who owns or is associated with this card.',
        on_delete=models.CASCADE,
    )
    card = models.ForeignKey(
        CardModel,
        related_name='user_card_associations',
        verbose_name='Card',
        help_text='The card that the user owns or is associated with.',
        on_delete=models.CASCADE,
    )
