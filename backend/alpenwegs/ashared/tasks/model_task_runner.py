# AlpenWegs import:
from alpenwegs.logger import app_logger

# Django/Celery imports:
from importlib import import_module
from celery import shared_task
from django.apps import apps

# Python import:
from typing import Union
from typing import Type

def resolve_service(
    service: Union[str, Type]
) -> Type:
    """
    Convert service_path string or type into a class.

    Raises ImportError / AttributeError if invalid.
    """

    # If provided parameter is already a class, return it directly
    if isinstance(service, type):
        # Return the class as-is:
        return service

    # Resolve provided string import path:
    if isinstance(service, str):
        # Split service_path into module path and class name:
        module_path, class_name = service.rsplit(".", 1)
        # Import module based on module path:
        module = import_module(module_path)
        # Get class from module:
        cls = getattr(module, class_name, None)
        # Verify if class was found:
        if cls is None:
            # Raise error if class has not been found:
            raise ImportError(f'Class "{class_name}" has not '
                f'been found in "{module_path}" path.'
            )
        # Return imported class:
        return cls

    # If neither a class nor a string was provided, raise error:
    raise TypeError('Parameter "service_path" must be either a class or a '
        f'string import path. Provided type is "{type(service).__name__}".'
    )

@shared_task(bind=True)
def model_task_runner(self,
    service_path: Union[str, Type],
    model_label: str,
    pk: str,
):
    """
    Universal Celery task runner for executing background processing
    against a Django model instance.

    This task provides a controlled mechanism to execute heavy or
    asynchronous operations outside of the request/response cycle.

    args:
        model_label (str):
            The Django model label in the format
            "app_label.ModelName" to identify the target model.
        pk (str):
            The primary key of the model instance to process.
        service_path (Union[str, Type]):
            The import path string or class
            of the service that contains the processing logic. The service
            class must implement a method `run_task(self, instance)`.

    returns:
        dict:
            A dictionary containing the status of the task execution,
            including success or error details.
    """

    # Collect model class:
    Model = apps.get_model(model_label)
    if Model is None:
        # Raise error if model could not be found:
        raise LookupError(f'Model "{model_label}" could not be found.')

    # Collect instance by pk value:
    instance = Model.objects.get(pk=pk)

    # Resolve service class from string or type:
    service_class = resolve_service(service_path)

    # Check if service class has run_task method:
    if not hasattr(service_class, "run_task"):
        # Raise error if method is missing:
        raise AttributeError(
            f'Provided service_path Class "{service_path}" must '
            'define run_task(self, instance).'
        )

    # Instantiate service:
    service = service_class(task_id=self.request.id)

    # Try to execute the service task:
    try:
        # Run the service task:
        result = service.run_task(instance)
    
    except Exception as exception:
        # Log error during run_task execution:
        app_logger.error(
            'Error occurred during run_task execution for service '
            f'"{service_path}" for instance {pk} ({model_label}). '
            f'Exception details: {exception}.',
        )
        # Return error response details:
        return {
            'status': 'error',
            'model': model_label,
            'pk': pk,
            'service': service_path,
            'result': None,
            'error': str(exception),
        }

    else:
        # Log successful execution of run_task method:
        app_logger.info(
            f'Service "{service_path}" successfully processed instance '
            f'{pk} ({model_label}). Result: {result}',
        )
        # Return success response details:
        return {
            'status': 'success',
            'model': model_label,
            'pk': pk,
            'service': service_path,
            'result': result,
            'error': None,
        }
