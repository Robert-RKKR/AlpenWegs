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

        def create_administrator():
            # Prepare administrator data:
            username = 'admin'
            email = 'admin@admin.com'
            password = 'admin'
            
            # Check if administrator exist:
            if UserModel.objects.filter(username=username).exists():
                # Get the administrator object:
                user = UserModel.objects.get(username=username)
                # Delete the administrator object:
                user.delete()
                # Log actions:
                self.stdout.write(self.style.SUCCESS(
                    f'3.0: Successfully deleted a old administrator.'))
            
            # Create a nwe administrator:
            return UserModel.objects.create_superuser(
                email,
                password,
                username=username,
            )
        
        try: # Try to make action:
            self.administrator = create_administrator()
        
        except Exception as exception:
            # Log action negatively accomplished:
            self.stdout.write(self.style.WARNING(
                '3.1: An error occurred while creating '
                f'a new administrator. Error: {exception}'))
        
        else:
            # Log action positively accomplished:
            self.stdout.write(self.style.SUCCESS(
                '3.1: Successfully created a new administrator.'))
            
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
