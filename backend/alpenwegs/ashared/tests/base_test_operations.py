# AlpenWegs import:
from alpenwegs.ashared.tests.base_test import BaseTest
from alpenwegs.logger import api_logger as logger

# Rest framework import:
from rest_framework.test import APITestCase
from django.urls import reverse
from django.apps import apps


# Base API test class:
class BaseApiTestOperations(
    BaseTest,
    APITestCase,
):

    # Scenarios data:
    scenario_objects = None
    scenario_tasks = None
    # Current scenario object data:
    current_object_relations = None
    current_object_data = None
    current_object_name = None
    # Current scenario task data:
    current_tasks_object_name = None


    def create_object(self,
        actor: str,
        model: str,
        data: dict,
        expected: int = 201,
    ) -> dict:
        """
        """

        # Collect URL from model:
        url = self._generate_api_url_list(model)
        
        
        logger.warning(f'url: {url}')

        payload = self._interpolate(data)
        logger.warning(f'payload: {payload}')

        r = self.request(actor=actor, method="post", url=url, data=payload, expected=expected)
        
        j = r.json()
        
        return j.get("page_results", j)
