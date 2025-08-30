# AlpenWegs import:
from alpenwegs.ashared.tests.base_test_operations import BaseApiTestOperations
from alpenwegs.logger import api_logger as logger

# Python import:
from rest_framework.test import APIClient
from dataclasses import dataclass


@dataclass
class Actor:
    client: APIClient
    password: str
    refresh: str
    access: str
    email: str
    name: str
    pk: str


# Base API test class:
class BaseApiTestActors(
    BaseApiTestOperations,
):
    
    # Default actor URLs:
    REGISTER_URL = '/api/auth/registration/'
    LOGOUT_URL = '/api/auth/logout/'
    LOGIN_URL = '/api/auth/login/'

    def setUp(self):
        # Call the parent setUp method:
        super().setUp()

        # Initialize actor dictionary:
        self.actors: dict[str, Actor] = {}

    def create_actor(self,
        username: str,
        email: str,
        password: str,
    ) -> str:
        """
        Create a new user and return the access code.
        """

        # Create API client instance:
        client = APIClient()

        # Create actor registration payload:
        register_payload = {
            'first_name': 'first_name',
            'last_name': 'last_name',
            'password1': password,
            'password2': password,
            'username': username,
            'email': email,
        }
        # Send registration request:
        response = client.post(
            path=self.REGISTER_URL,
            data=register_payload,
            format='json'
        )

        # Check if registration was successful:
        if response.status_code == 201:
            # Convert json response to dictionary:
            data = response.json()
            # Collect actor access and refresh code:
            refresh = data.get('page_data', {}).get('refresh', '')
            access = data.get('page_data', {}).get('access', '')
            # Collect actor PK number:
            pk = data.get('page_data', {}).get('user_id', '')
            # Create actor entry:
            self.actors[username] = Actor(
                password=password,
                name=username,
                client=client,
                refresh=refresh,
                access=access,
                email=email,
                pk=pk,
            )

        else:
            # Raise an assertion error:
            raise AssertionError('User creation failed for actor '
                f'{username}. Status code: {response.status_code}, '
                f'Response: {data}.'
            )

    def login_actor(self,
        username: str,
    ) -> str:
        """
        Log in user and return the access code.
        """

        # Collect actor object:
        actor = self.actors[username]

        # Create actor login payload:
        login_payload = {
            'password': actor.password,
            'email': actor.email,
        }
        # Send login request:
        response = actor.client.post(
            path=self.LOGIN_URL,
            data=login_payload,
            format='json'
        )

        # Check if login was successful:
        if response.status_code == 200:
            # Convert json response to dictionary:
            data = response.json()
            # Collect and return actor access code:
            return data.get('page_data', {}).get('access', '')

        else:
            # Raise an assertion error:
            raise AssertionError(f'Login failed for actor {username}. '
                f'Status code: {response.status_code}, Response: {data}.'
            )

    def logout_actor(self,
        username: str,
    ) -> bool:
        """
        Log out user and return the success status.
        """

        # Collect actor object:
        actor = self.actors[username]

        # Create actor logout payload:
        logout_payload = {
            'refresh': actor.refresh,
        }
        # Send logout request:
        response = actor.client.post(
            path=self.LOGOUT_URL,
            data=logout_payload,
            format='json',
        )

        # Check if logout was successful:
        if response.status_code == 200:
            # Clear actor credentials:
            actor.client.credentials()
            # Return success response:
            return True

        else:
            # Raise an assertion error:
            raise AssertionError(f'Logout failed for actor {username}. '
                f'Status code: {response.status_code}.'
            )
