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
        email: str,
        password: str = None,
        **extra_fields: dict,
    ):
        """
        Method to create and return a new member.
        """

        # Validate member mail:
        email = self.normalize_email(email)

        # Provide member extra fields:
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        # Create a new user member instance with the provided data:
        member = self.model(
            email=email,
            **extra_fields
        )

        # Set member password:
        if password:
            member.set_password(password)
        else:
            member.set_unusable_password()

        # Save the member instance:
        member.save(using=self._db)

        # Return the created member instance:
        return member
    
    def create_superuser(self,
        email: str,
        password: str,
        **extra_fields: dict,
    ):
        """
        Method to create and return a new super member.
        """

        # Provide member extra fields:
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Create a new superuser member instance with the provided data:
        member = self.create_user(
            email=email,
            password=password,
            **extra_fields,
        )
        
        # Return the created member instance:
        return member
