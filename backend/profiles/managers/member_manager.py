# Django user manager import:
from django.contrib.auth.models import BaseUserManager


# Member Profile manager class:
class MemberProfileManager(BaseUserManager):
    """
    Manager for MemberModel, providing methods to create user and
    superuser profiles. This manager handles the creation of user
    profiles with necessary fields and ensures that the email
    is unique and properly formatted.
    """

    def create_user(self,
        name: str,
        email: str,
        password: str = None,
        **extra_fields
    ):
        """
        Method to create and return a new member.
        """

        # Create a new user member instance with the provided data:
        member = self.model(name=name, email=email, **extra_fields)
        member.set_password(password)
        member.save(using=self._db)

        # Return the created member instance:
        return member
    
    def create_superuser(self,
        name: str,
        email: str,
        password: str
    ):
        """
        Method to create and return a new super member.
        """

        # Create a new superuser member instance with the provided data:
        member = self.create_user(name, email, password)
        member.is_staff = True
        member.is_superuser = True
        member.save(using=self._db)

        # Return the created member instance:
        return member
