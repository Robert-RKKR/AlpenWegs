"""
Abstract Base Model for Descriptive
---------------------------------------------------------

This abstract base model is designed to provide a descriptive role
for inherited models. It extends model with a detailed `description`
field.

The `description` field is flexible and may contain plain text,
rich text, or Markdown, allowing creators to document context such
as terrain, difficulty, notable landmarks, scenic highlights,
or other user-provided insights.
"""

# AlpenWegs import:
from .base_model import BaseModel

# Django import:
from django.db import models


# Base Descriptive models class:
class BaseDescriptiveModel(
    BaseModel, 
):
    """
    Abstract base class that provides descriptive capabilities.

    In addition to identification attributes (handled by BaseModel),
    this model introduces a `description` field for extended,
    user-defined content. The description can be written in plain
    text, rich text, or Markdown.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Base Descriptive Model'
        verbose_name_plural = 'Base Descriptive Models'

        # Abstract class value:
        abstract = True

    # Descriptive model values:
    description = models.TextField(
        verbose_name='Object Description',
        help_text='A detailed description of the object. Supports plain '
            'text, rich text, or Markdown. Intended for contextual details '
            'such as terrain, difficulty level, notable landmarks, scenic '
            'highlights, and any other creator-provided insights.',
        blank=True,
        null=True,
    )
