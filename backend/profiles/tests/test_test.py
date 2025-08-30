from alpenwegs.ashared.tests.base_test_actors import BaseApiTestActors
from profiles.models.user_model import UserModel
from alpenwegs.logger import test_logger as logger


class UserApiTest(BaseApiTestActors):

    def test(self):

        self.create_actor(
            username="testuser",
            email="testuser@example.com",
            password="!Securepassword#123",
        )

        access_code = self.login_actor(
            username="testuser"
        )

        logger.warning(f'access_code: {access_code}')

        status = self.logout_actor(
            username="testuser"
        )
        logger.warning(f'status: {status}')
