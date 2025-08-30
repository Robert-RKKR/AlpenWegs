# AlpenWegs import:
from alpenwegs.ashared.models.base_model import BaseModel

# Django import:
from django.core.exceptions import ImproperlyConfigured
from django.core.exceptions import ObjectDoesNotExist
from django.apps import apps

# Collect object data function:
def collect_object_data(
    instance: BaseModel
) -> dict:
    """
    Function collect object data from provided object.

    Returns (dict):
        - app_name = Name of the object application.
        - model_name = Name of the object model.
        - object_id = Correlated object PK representation.
        - object_representation = Object representation.
    """

    # Check if instance belongs or inherits from BaseModel class:
    if isinstance(instance, BaseModel):
        try: # Try to collect object representation:
            object_representation = instance.name
        except:
            object_representation = instance.pk
        finally:
            try: # Try to collect object related information:
                application_name = instance.__class__._meta.app_label
                model_name = instance.__class__.__name__
                object_id = instance.pk
            except:
                application_name = None
                model_name = None
                object_id = None
            finally:
                object_related_data = {
                    'app_name': application_name,
                    'model_name': model_name,
                    'object_representation': object_representation,
                    'object_id': object_id}
                # Return collected data:
                return object_related_data
    else:
        # Raise type error if instance doesn't inherits from BaseModel class:
        raise TypeError('Provided instance value is not valid object.')

def collect_model(
    app_name: str,
    model_name: str
) -> BaseModel:
    """
    Retrieve and return a Django model class based on a given string.

    Args:
        app_name (str):
            Name of the Capybara application.
        model_name (str):
            Name of the Capybara model.

    Returns (BaseModel):
        BaseModel or raises an appropriate error if not found.
    """

    try: # Try to retrieve the model class based on app_label and model_name:
        model = apps.get_model(app_name, model_name)
    except (LookupError, ImproperlyConfigured):
        # If model is None, raise an appropriate error:
        raise LookupError(f'Model "{app_name}:{model_name}" could not be found.')
    # Return the model class
    return model

def collect_object(
    app_name: str,
    model_name: str,
    object_id: int
) -> BaseModel:
    """
    Retrieve and return a specific Django model object based on:
    app_name, model_name, and object_id.

    Args:
        app_name (str):
            Name of the Capybara application.
        model_name (str):
            Name of the Capybara model.
        object_id (int):
            The primary key or ID of the object to retrieve.
    
    Returns (BaseModel):
        BaseModel instance or raises an appropriate error if not found.
    """

    # First, use the collect_model function to get the model class:
    model_class = collect_model(app_name, model_name)
    try: # Try to get the object by its primary key:
        obj = model_class.objects.get(pk=object_id)
    except ObjectDoesNotExist:
        # If the object doesn't exist, raise an appropriate error:
        raise ObjectDoesNotExist(f'Object with id "{object_id}" not '
            f'found in model "{app_name}:{model_name}".')
    # Return the object
    return obj
