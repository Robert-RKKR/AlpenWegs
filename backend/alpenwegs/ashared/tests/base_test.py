# AlpenWegs import:
from alpenwegs.ashared.models.base_model import BaseModel
from alpenwegs.logger import test_logger as logger

# Python import:
from django.urls import reverse
from django.apps import apps
import inspect
import yaml
import os
import re



# Base API test class:
class BaseTest():

    def setUp(self) -> None:
        """
        Set Up base API test settings like:
            - Global application settings.
            - Logger initiation.
        """

        # Initiate logger:
        self.logger = logger

    def _camel_to_snake(self,
        name: str
    ) -> str:
        """
        Convert camel case to snake case.
        """

        # Convert camel case to snake case:
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        # Convert any remaining uppercase letters to lowercase:
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def _get_model_name(self,
        model_class: BaseModel
    ) -> str:
        """
        Get the model name in lowercase.
        """

        # Get the model name in lowercase:
        return self._camel_to_snake(
            model_class.__name__
        )

    def _get_class_name(self,
        model_class: BaseModel) -> str:
        """
        Get the class name in lowercase.
        """

        # Get the class name in lowercase:
        return model_class._meta.app_label.lower()

    def _generate_api_url_list(self,
        model_class: BaseModel) -> str:
        """
        Generate the API URL for listing objects based on the model class name.
        Uses the Django REST framework naming convention for list views.
        """

        # Get the model and class name in lowercase:
        app_name = self._get_class_name(model_class)
        model_name = self._get_model_name(model_class)
        # Construct the API URL name using the API pattern:
        api_url_name = f'api-{app_name}:{model_name}-list'
        
        # Return URL:
        return reverse(api_url_name)

    def _generate_api_url_detail(self,
        model_class: BaseModel,
        object_id: str) -> str:
        """
        Generate the API URL for retrieving a single object by ID.
        Uses the Django REST framework naming convention for detail views.
        """

        # Get the model and class name in lowercase:
        app_name = self._get_class_name(model_class)
        model_name = self._get_model_name(model_class)
        # Construct the API URL name using the API pattern:
        api_url_name = f'api-{app_name}:{model_name}-detail'
        
        # Return URL:
        return reverse(api_url_name, args=[object_id])
    
    def _get_model_by_name(self,
            app_name: str,
            model_name: str) -> BaseModel:
        """
        Collect django model based on app and model name.
        """

        try:
            # Try to collect django model:
            return apps.get_model(
                app_label=app_name,
                model_name=model_name
            )

        except LookupError:
            # Raise error if not found:
            return None
    
    def _collect_scenarios(self,
        scenario_filename: str) -> str:
        """
        Collect test case scenarios from YAML file. The YAML filename is based
        on the model name ended with .yaml and is located in 'scenarios' folder
        in the same directory as the test class file.
        """

        # Get the directory of the current file
        current_file_directory = os.path.dirname(inspect.getfile(self.__class__))
        # Construct the full path to the scenarios file:
        scenario_full_path = os.path.join(
            current_file_directory, 'scenarios', scenario_filename)
        
        try:
            # Try to load scenarios from YAML file:
            with open(scenario_full_path, 'r') as file:
                # Collect all scenarios:
                all_scenarios = yaml.safe_load(file)
        
        except Exception as exception:
            # Raise an error if there is a problem reading the test scenario file:
            raise FileExistsError('An error has occurred while opening '\
                'or reading a file, with test scenarios. Scenario path: '\
                f'{scenario_full_path}. Error: {exception}')
        
        # Return scenarios:
        return all_scenarios
