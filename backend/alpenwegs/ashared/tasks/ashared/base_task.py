# Alpenwegs import:
from alpenwegs.logger import app_logger

# Python import:
from datetime import timedelta


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
    
    def _decimal_accuracy(self,
        value: float,
        places: int = 2,
    ) -> float:
        """
        Round a float value to specified decimal places.
        """

        # Check if value is not None:
        if isinstance(value, float):
            # Return rounded value:
            return round(value, places)
        
        elif isinstance(value, int):
            # Return integer as float:
            return float(value)
        
        else:
            # Return None if value is None:
            return None

    @staticmethod
    def _safe_timedelta_seconds(value):
        """
        Convert timedelta to seconds as float.
        """

        # Check if value is timedelta:
        if isinstance(value, timedelta):
            return float(value.total_seconds())
        
        else:
            # Return None if value is not timedelta:
            return None
