# Django user manager import:
from django.contrib.auth.models import BaseUserManager


# User Profile manager class:
class UserProfileManager(BaseUserManager):
    """
    Manager for UserModel, providing methods to create user and
    superuser profiles. This manager handles the creation of user
    profiles with necessary fields and ensures that the email
    is unique and properly formatted.
    """

    def create_user(self,
        email: str,
        password: str = None,
        **extra_fields: dict,
    ):
        """
        Method to create and return a new user.
        """

        # Validate user mail:
        email = self.normalize_email(email)

        # Provide user extra fields:
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        # Create a new user user instance with the provided data:
        user = self.model(
            email=email,
            **extra_fields
        )

        # Set user password:
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        # Save the user instance:
        user.save(using=self._db)

        # Return the created user instance:
        return user
    
    def create_superuser(self,
        email: str,
        password: str,
        **extra_fields: dict,
    ):
        """
        Method to create and return a new super user.
        """

        # Provide user extra fields:
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Create a new superuser user instance with the provided data:
        user = self.create_user(
            email=email,
            password=password,
            **extra_fields,
        )
        
        # Return the created user instance:
        return user
