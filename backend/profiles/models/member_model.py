# Application import:
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel

# Component import:
from profiles.managers.member_manager import MemberProfileManager

# Django import:
from django.db import models


# Member model class:
class MemberModel(
    BaseTimestampModel
):

    class Meta:

        # Model name values:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    # Model objects manager:
    objects = MemberProfileManager()

    # Main Member information:
    email = models.EmailField(
        verbose_name='E-mail address',
        help_text='The user\'s unique email address, which serves as the '
            'primary authentication credential and unique identifier '
            'within the system. This email is required for logging in, '
            'password recovery, and receiving notifications or updates. '
            'Each email must be unique to ensure proper identification '
            'and prevent duplication of accounts.',
        max_length=255,
        unique=True,
    )

    # Password information:
    password_to_change = models.BooleanField(
        verbose_name='Password change required',
        help_text='Indicates whether the user must change their '
            'password upon next login. This is typically set after an '
            'initial account setup or password reset to enhance '
            'security and ensure the user has set a personalized password.',
        default=False,
    )

    # Name detailed information:
    first_name = models.CharField(
        verbose_name='First Name',
        help_text='The user\'s given name, used for personalized '
            'communication. This field is required for proper user '
            'identification. It helps in addressing the user in messages, '
            'emails, and other interactions within the system.',
        max_length=128,
        blank=True,
        null=False,
    )
    middle_name = models.CharField(
        verbose_name='Middle Name',
        help_text='An optional middle name field for users who have '
            'multiple given names. This can provide more precise '
            'identification but is not mandatory.',
        max_length=128,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        help_text='The user\'s surname name, used for personalized '
            'communication. This field is required for proper user '
            'identification. It helps in addressing the user in messages, '
            'emails, and other interactions within the system.',
        max_length=128,
        blank=True,
        null=False,
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
    gender = models.CharField(
        verbose_name='Gender',
        help_text='User\'s gender. This field can be used to '
            'personalize the user experience and address the '
            'user properly. It is optional.',
        max_length=32,
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
            'calculated using the user\'s weight and height. '
            'This field is optional.',
        blank=True,
        null=True,
    )
    birthday = models.DateTimeField(
        verbose_name='Birthday',
        help_text='User\'s birthdate. This can be used to '
            'calculate the user\'s age or personalize content.'
            'This field is optional.',
        blank=True,
        null=True,
    )

    # Location information:
    location = models.CharField(
        verbose_name='Location',
        help_text='User\'s geographic location, which '
            'could be used for personalization or for tracking '
            'user activity. This field is optional.',
        max_length=128,
        blank=True,
        null=True,
    )
    location_name = models.CharField(
        verbose_name='Location Name',
        help_text='User\'s location name, such as city, '
            'town, or landmark. This field provides additional '
            'context to the user\'s geographical location and '
            'can help personalize their experience.',
        max_length=128,
        blank=True,
        null=True,
    )

    def set_password(self, raw_password):
        """
        Set the password for the user. Also sets `password_to_change` to False.
        """

        self.password_to_change = False
        super().set_password(raw_password)
