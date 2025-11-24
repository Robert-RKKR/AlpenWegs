# AlpenWegs application import:
from notifications.models.change_log_model import ChangeLogModel
from profiles.models.user_model import UserModel

# AlpenWegs import:
from alpenwegs.ashared.constants.action_type import ActionTypeChoices
from alpenwegs.ashared.models.base_model import BaseModel
from alpenwegs.logger import app_logger

# Django import:
from django.core.serializers import serialize

# Python import:
import json

def collect_names(sender):
    """
    Collect base content type information,
    like application and model names.
    """

    # Try to collect base content type information:
    try:
        app_name = sender._meta.app_label
        model_name = sender.__name__
    except:
        app_name = None
        model_name = None

    # Return names toupee:
    return (app_name, model_name)

def collect_object_representation(
    instance,
):
    """
    Collect object representation,
    like natural key or name or pk / id.
    """

    try: 
        # Try to collect object representation.
        # Collect natural key like object representation:
        object_representation = instance.natural_key()
    
    except:
        try:
            # Try to collect name value like object representation:
            object_representation = instance.name
        
        except:
            # If object doesn't have name value:
            try:
                # Try to collect PK / ID value like object representation:
                object_representation = instance.pk
            
            except: # Return non like object representation:
                return None
    
    # Return object representation:
    return object_representation

def log_change(
    instance: BaseModel,
    user: UserModel,
    action: ActionTypeChoices,
) -> ChangeLogModel:
    """
    Logs the change made to the provided instance.
    """

    # Check collected data:
    if not isinstance(user, UserModel):
        raise TypeError('Provided user is not a valid AlpenWegs user model.')
    if not isinstance(
        instance, BaseModel) and not isinstance(instance, UserModel):
        raise TypeError('Provided instance is not a valid AlpenWegs model.')

    # Collect sender class:
    sender = instance.__class__
    # Collect object content:
    json_str = serialize('json', [instance], use_natural_foreign_keys=True,
        use_natural_primary_keys=True)
    object_data = json.loads(json_str)[0]['fields']
    # Collect base content type information:
    app_name, model_name = collect_names(sender)
    
    try:
        # Create a new change log:
        change_log = ChangeLogModel.objects.create(
            object_repr=collect_object_representation(instance),
            model_name=model_name,
            object_id=instance.pk,
            action_type=action,
            app_name=app_name,
            after=object_data,
            creator=user,
        )
   
    except Exception as exception:
        # Log error if change log creation fails:
        app_logger.error(exception)
        return False
    
    else:
        # Return created change log:
        return change_log
