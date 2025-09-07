# Django import:
from django.core.management.base import CommandError
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django.apps import apps

# AlpenWegs application import:
from profiles.models.user_model import UserModel

# Define allowed actions:
ALLOWED_ACTIONS = [
    'view',
    'add',
    'change',
    'delete',
]

# Command class:
class Command(BaseCommand):
    help = 'Creates a default administrator if none exists'

    def create_default_administrator(self):

        def create_user(
            super_user: bool,
            first_name: str,
            last_name: str,
            password: str,
            username: str,
            email: str,
        ):
            
            # Check if user exist:
            if UserModel.objects.filter(username=username).exists():
                # Get the user object:
                user = UserModel.objects.get(
                    username=username,
                )
                # Delete the user object:
                user.delete()
                # Log actions:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'3.0: Successfully deleted a old user.'
                    )
                )

            # Create a new user:
            if super_user:
                # Create a new super user:
                user = UserModel.objects.create_superuser(
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                    username=username,
                    email=email,
                )

            else:
                # Create a new regular user:
                user = UserModel.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                    username=username,
                    email=email,
                )

            # Log action positively accomplished:
            self.stdout.write(
                self.style.SUCCESS(
                    f'3.1: Successfully created a new {username} user.'
                )
            )
            # Return created user:
            return user

        self.member = create_user(
            super_user=False,
            email='member@alpenwegs.com',
            first_name='First',
            last_name='Last',
            password='sfsefsef3434@!$2',
            username='Member'
        )
        self.author = create_user(
            super_user=False,
            email='author@alpenwegs.com',
            first_name='First',
            last_name='Last',
            password='sfsefsef3434@!$2',
            username='Author'
        )
        self.admin = create_user(
            super_user=False,
            email='admin@alpenwegs.com',
            first_name='First',
            last_name='Last',
            password='sfsefsef3434@!$2',
            username='Admin'
        )
        self.administrator = create_user(
            super_user=True,
            email='administrator@alpenwegs.com',
            first_name='First',
            last_name='Last',
            password='sfsefsef3434@!$2',
            username='Administrator'
        )
            
    def apply_role_permissions(self):
        """
        Collect ROLE_PERMS / access_* from models and add the matching
        permissions to Member / Author / Admin groups.
        """

        # Fetch created groups:
        roles = {
            'Member': Group.objects.get(name='Member'),
            'Author': Group.objects.get(name='Author'),
            'Admin':  Group.objects.get(name='Admin'),
        }

        # Iterate over all models in the application:
        for model in apps.get_models():
            # Collect role permissions from model:
            role_perms = getattr(model, 'ROLE_PERMS', {})
            # Collect model name:
            model_name = model._meta.model_name
            
            # Iterate over defined roles:
            for role, group in roles.items():
                # Collect model permissions for the role:
                permission_actions = role_perms.get(role, [])

                # Iterate over permission actions to assign permissions:
                for permission_action in permission_actions:
                    # Check if requested action is allowed:
                    if permission_action not in ALLOWED_ACTIONS:
                        raise CommandError(
                            f'3.2: The action "{permission_action}" is not allowed. '
                            'Please use one of the following actions: '
                            f'"{", ".join(ALLOWED_ACTIONS)}".'
                        )
                    # Collect permission object based on action and model name:
                    permission = Permission.objects.get(
                        codename=f'{permission_action}_{model_name}')
                    # Add permission to the group:
                    group.permissions.add(permission)

        # Log action positively accomplished:
        self.stdout.write(self.style.SUCCESS(
            '2.1: Successfully added all permissions to groups.'))

    def create_default_groups(self):

        # Create default groups:
        Group.objects.get_or_create(name='Member')
        Group.objects.get_or_create(name='Author')
        Group.objects.get_or_create(name='Admin')
        # Log action positively accomplished:
        self.stdout.write(self.style.SUCCESS(
            '1.1: Successfully created all base groups.'))

    def handle(self, *args, **options):
        
        # 1: Create default groups:
        self.create_default_groups()

        # 2: Apply role permissions:
        self.apply_role_permissions()

        # # 3: Create default administrator:
        self.create_default_administrator()
