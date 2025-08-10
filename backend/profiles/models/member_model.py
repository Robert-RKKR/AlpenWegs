# Application import:
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel
from alpenwegs.ashared.constants.gender_type import GenderTypeChoices

# Component import:
from profiles.managers.member_manager import MemberProfileManager

# Django import:
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.functions import Lower
from django.db.models import Q
from django.db import models


# Member model class:
class MemberModel(
    BaseTimestampModel,
    AbstractBaseUser,
    PermissionsMixin,
):

    class Meta:

        # Model name values:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

        # Model constraints:
        constraints = [
            models.UniqueConstraint(
                Lower('email'),
                name='uniq_member_email_lower',
            ),
            models.CheckConstraint(
                check=Q(height__isnull=True) | Q(height__gt=0),
                name="height_gt_zero_or_null",
            ),
            models.CheckConstraint(
                check=Q(weight__isnull=True) | Q(weight__gt=0),
                name="weight_gt_zero_or_null",
            ),
        ]

    # Model objects manager:
    objects = MemberProfileManager()

    # Required Member fields:
    is_active = models.BooleanField(
        verbose_name='Is Active',
        help_text='Indicates whether the member account is active.',
        default=True,
    )
    is_staff = models.BooleanField(
        verbose_name='Is Staff',
        help_text='Indicates whether the member has staff privileges.',
        default=False,
    )

    # Base Member identification information:
    email = models.EmailField(
        verbose_name='E-mail address',
        help_text='The member\'s unique email address, which serves as the '
            'primary authentication credential and unique identifier '
            'within the system. This email is required for logging in, '
            'password recovery, and receiving notifications or updates. '
            'Each email must be unique to ensure proper identification '
            'and prevent duplication of accounts.',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name='First Name',
        help_text='The member\'s given name, used for personalized '
            'communication. This field is required for proper member '
            'identification. It helps in addressing the member in messages, '
            'emails, and other interactions within the system.',
        max_length=128,
        blank=True,
        null=False,
    )
    middle_name = models.CharField(
        verbose_name='Middle Name',
        help_text='An optional middle name field for members who have '
            'multiple given names. This can provide more precise '
            'identification but is not mandatory.',
        max_length=128,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        help_text='The member\'s surname name, used for personalized '
            'communication. This field is required for proper member '
            'identification. It helps in addressing the member in messages, '
            'emails, and other interactions within the system.',
        max_length=128,
        blank=True,
        null=False,
    )

    # Password information:
    password_to_change = models.BooleanField(
        verbose_name='Password change required',
        help_text='Indicates whether the member must change their '
            'password upon next login. This is typically set after an '
            'initial account setup or password reset to enhance '
            'security and ensure the member has set a personalized password.',
        default=False,
    )

    # Contact information:
    phone_number = models.BigIntegerField(
        verbose_name='Phone number',
        help_text='User\'s phone number. It can be used for '
            'communication purposes such as account recovery or '
            'urgent notifications. This field is optional.',
        null=True,
        blank=True
    )

    # Personal information:
    gender = models.IntegerField(
        verbose_name='Gender',
        help_text='User\'s gender. This field can be used to '
            'personalize the member experience and address the '
            'member properly. It is optional.',
        choices=GenderTypeChoices.choices,
        blank=True,
        null=True,
    )
    weight = models.FloatField(
        verbose_name='Weight',
        help_text='User\'s weight in kilograms. This can be '
            'used to track health data or fitness goals. '
            'This field is optional.',
        blank=True,
        null=True,
    )
    height = models.FloatField(
        verbose_name='Height',
        help_text='User\'s height in centimeters. This '
            'can be used to track health data or fitness goals. '
            'This field is optional.',
        blank=True,
        null=True,
    )
    bmi = models.FloatField(
        verbose_name='BMI',
        help_text='User\'s Body Mass Index (BMI). It is '
            'calculated using the member\'s weight and height. '
            'This field is optional.',
        blank=True,
        null=True,
    )
    birthday = models.DateTimeField(
        verbose_name='Birthday',
        help_text='User\'s birthdate. This can be used to '
            'calculate the member\'s age or personalize content.'
            'This field is optional.',
        blank=True,
        null=True,
    )

    # Location information:
    location = models.CharField(
        verbose_name='Location',
        help_text='User\'s geographic location, which '
            'could be used for personalization or for tracking '
            'member activity. This field is optional.',
        max_length=128,
        blank=True,
        null=True,
    )
    location_name = models.CharField(
        verbose_name='Location Name',
        help_text='User\'s location name, such as city, '
            'town, or landmark. This field provides additional '
            'context to the member\'s geographical location and '
            'can help personalize their experience.',
        max_length=128,
        blank=True,
        null=True,
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self) -> str:

        parts = [self.first_name or '', self.middle_name or '', self.last_name or '']
        return " ".join(p for p in parts if p).strip()

    def get_short_name(self) -> str:

        return self.first_name or self.email

    property
    def bmi(self) -> float | None:
        """
        Compute BMI on the fly from height (cm) and weight (kg).
        """

        if not self.height or not self.weight:
            return None
        h_m = self.height / 100.0
        if h_m <= 0:
            return None
        return round(self.weight / (h_m * h_m), 1)

    def set_password(self, raw_password):
        """
        Set the password and clear 'password_to_change'.
        """

        self.password_to_change = False
        super().set_password(raw_password)

    def representation(self):
        return f'{self.first_name} {self.last_name}'