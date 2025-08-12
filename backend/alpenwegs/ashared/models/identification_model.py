"""
Abstract Base Model for Identification
---------------------------------------------------------

This abstract base model is designed to handle identification attributes 
like `name` and `slug`. It includes automatic slug generation 
based on the `name` field and provides additional object description
`snippet`.

This model is meant to be inherited by other models that require these 
identification fields.
"""

# AlpenWegs import:
from alpenwegs.ashared.validators.base_validators import DescriptionValueValidator
from alpenwegs.ashared.validators.base_validators import NameValueValidator
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel

# Django import:
from django.template.defaultfilters import slugify
from django.db import models


# Base Identification models class:
class BaseIdentificationModel(
    BaseTimestampModel, 
):
    """
    An abstract base model for handling identification attributes 
    and generating slugs for objects.

    Intended for use by models that need these identification fields.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Base Identification Model'
        verbose_name_plural = 'Base Identification Models'

        # Abstract class value:
        abstract = True

        # Default ordering:
        ordering = ['name']

    # Model validators:
    name_validator = NameValueValidator()
    description_validator = DescriptionValueValidator()

    # Identification model values:
    name = models.CharField(
        verbose_name='Name',
        help_text='A unique name for the object. Must be between '
            '3 and 128 characters long and can include letters, digits, '
            'spaces, or special characters such as -, _, and spaces. '
            'This field does not serve as a unique identifier within the '
            'application but helps users differentiate it from other objects.',
        validators=[name_validator],
        max_length=128,
        unique=True,
    )
    slug = models.CharField(
        verbose_name='Slug',
        help_text='A unique, URL-friendly version of the name, '
            'automatically generated from the object\'s name. This field '
            'is used for SEO and as an identifier in URLs.',
        max_length=128,
    )
    snippet = models.CharField(
        verbose_name='Snippet',
        help_text='A short description of the object, between 8 and 256 '
            'characters. It may include letters, numbers, spaces, and '
            'the special characters -, _, and .',
        validators=[description_validator],
        max_length=256,
        blank=True,
        null=True,
    )

    # object representation:
    def object_representation(self):
        """
        Return object string representation.
        """

        return self.name

    def _generate_slug(self):
        """
        Generate slug for all objects.
        """

        # Create slug based on provided name value:
        self.slug = slugify(self.name)

    def _generate_snippet(self):
        """
        Generate snippet if not provided.
        """

        # Create default object snippet if not provided:
        if not self.snippet:
            self.snippet = f'{self.model_representation()} '\
                'object default snippet.'

    # Run dedicated operation function:
    def dedicated_operation(self):
        # Call the original dedicated_operation method:
        super().dedicated_operation()
        # Create slug based on provided name value:
        self._generate_slug()
        # Create default object snippet if not provided:
        self._generate_snippet()
