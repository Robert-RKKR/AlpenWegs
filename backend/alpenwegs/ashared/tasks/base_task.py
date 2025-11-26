# Alpenwegs import:
from alpenwegs.logger import app_logger


# Base Task Class:
class BaseTask:
    """
    Base class for all background-processing services.

    Provides:
        self.name: Logical name of the task class.
        self.logger: Common application logger.
        self.task_id: Celery task ID injected by model_task_runner.
    """

    def __init__(self,
        name: str = None,
        task_id: str = None,
    ) -> None:
        """
        Initialize base task properties.
        """
    
        # Define base task properties:
        self.name = name or self.__class__.__name__
        self.logger = app_logger
        self.task_id = task_id

    def execute(self, 
        *args,
        **kwargs,
    ) -> None:
        """
        Must be implemented by all subclasses.
        """

        # Enforce implementation in subclasses:
        raise NotImplementedError(
            'Subclasses must implement the `execute()` method.'
        )

    def run_task(self,
        instance,
    ) -> None:
        """
        Entry point for model_task_runner.
        Services may override this to use instance-based processing.
        """

        # Default implementation calls execute():
        return self.execute(instance)
