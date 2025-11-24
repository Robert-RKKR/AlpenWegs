"""
Abstract Base Model for Standardized Object Management
------------------------------------------------------

This model provides a foundational structure for all application models, 
ensuring each object has a unique identifier and built-in lifecycle 
management methods.

Key Features:
- Unique ID (UUIDv4) as the primary key.
- Standardized model representation.
"""

# Django import:
from django.db import transaction
from django.db import models

# Python import:
import uuid
import re


# Base model class:
class BaseModel(
    models.Model,
):
    """
    An abstract base model that assigns a unique ID to each
    object and includes built-in methods for validation,
    representation, and lifecycle management.
    
    The BaseModel is a key component of all other base models
    and all standard application models. This means that all
    other application models should inherit directly from
    the BaseModel, or indirectly from any other base model
    such as BaseTimestampModel or BaseIdentificationModel.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Base model'
        verbose_name_plural = 'Base models'

        # Abstract class value:
        abstract = True

        # Default ordering:
        ordering = ['id']


    # Primary Key value:
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name='ID',
        help_text='A unique identifier for the object, '
            'automatically generated as a UUIDv4 value.'
    )


    #=================================================================
    # Object statistic methods:
    #=================================================================
    @classmethod
    def show_count_all(cls) -> int:
        """
        Return number of existing model objects.
        """

        return cls.objects.count()

    #=================================================================
    # Object representation:
    #=================================================================
    def __repr__(self) -> str:
        """
        Model object representation:
        """

        # Collect model representation name:
        model_rep = self.model_representation()
        # Collect object representation name:
        object_rep = self.object_representation()
        # Return object representation:
        return f'<Class {model_rep}: {object_rep}>'

    def __str__(self) -> str:
        """
        Return model object string representation.
        """
        
        # Return object representation:
        return self.representation()

    def natural_key(self) -> str:
        """
        Return model object string representation.
        """
        
        # Return object representation:
        return self.representation()

    def representation(self) -> str:
        """
        Return model string representation.
        """

        # Collect model representation name:
        model_rep = self.model_representation()
        # Collect object representation name:
        object_rep = self.object_representation()
        # Return object representation:
        return f'<Class {model_rep} ({object_rep})>'

    def model_representation(self) -> str:
        """
        Return model string representation.
        """

        # Collect model name:
        model_name = self.__class__.__name__
        # Convert and return camel case to space-separated model name:
        return re.sub(r'(?<!^)(?=[A-Z])', ' ', model_name).replace('_', ' ')

    def object_representation(self) -> str:
        """
        Return object string representation.
        """

        return f'ID: {self.id}'

    #=================================================================
    # Additional representation methods:
    #=================================================================
    def as_dictionary(self) -> dict:
        """
        Return all attributes of the instance as a dictionary.
        """

        return {
            field.name: getattr(self, field.name)
            for field in self._meta.fields
        }

    #=================================================================
    # Methods run before and after saving model objects:
    # =================================================================
    def run_before_validation(self) -> None:
        """
        Custom logic to be executed before validating the model.
        This method can be overridden in derived classes.
        """

        pass

    def run_after_validation(self) -> None:
        """
        Custom logic to be executed after validating the model.
        This method can be overridden in derived classes.
        """

        pass

    def run_before_save(self) -> None:
        """
        Custom logic to be executed before saving the model.
        This method can be overridden in derived classes.
        """

        pass

    def run_after_save(self) -> None:
        """
        Custom logic to be executed after saving the model.
        This method can be overridden in derived classes.
        """

        pass

    #=================================================================
    # Celery async method to run after commit:
    #=================================================================
    def run_after_commit(self,
        created: bool,
    ) -> None:
        """
        Custom logic to be executed after the database transaction
        is committed. Intended ONLY for scheduling asynchronous tasks
        (e.g. Celery), not for heavy synchronous processing.
        """
        
        pass

    #=================================================================
    # Override save and full clean method to include custom logic:
    # =================================================================
    def full_clean(self, *args, **kwargs):
        """
        Override the full_clean method to include custom logic
        before and after validation.
        """

        # Run custom logic before validation:
        self.run_before_validation()

        # Call the parent class's full_clean method:
        super().full_clean(*args, **kwargs)

        # Run custom logic after validation:
        self.run_after_validation()

    def save(self, *args, **kwargs):
        """
        Override the save method to include custom logic
        before and after saving.
        """

        # Determine if the instance is new:
        is_new = self._state.adding

        # Run custom logic before saving:
        self.run_before_save()

        # Call the parent class's save method:
        super().save(*args, **kwargs)

        # Run custom logic after saving:
        self.run_after_save()

        # Schedule async hooks AFTER COMMIT:
        transaction.on_commit(
            lambda: self.run_after_commit(is_new)
        )
