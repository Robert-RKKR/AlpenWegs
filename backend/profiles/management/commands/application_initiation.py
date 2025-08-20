# Django - import:
from django.core.management.base import CommandError
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group

# Capybara - import:
from profiles.models.user_model import UserModel


# Command class:
class Command(BaseCommand):
    help = 'Creates a default administrator if none exists'

    def create_default_administrator(self):

        def create_administrator():
            # Prepare administrator data:
            username = 'admin'
            email = 'admin@capybara.com'
            password = 'admin'
            
            # Check if administrator exist:
            if UserModel.objects.filter(username=username).exists():
                # Get the administrator object:
                user = UserModel.objects.get(username=username)
                # Delete the administrator object:
                user.delete()
                # Log actions:
                self.stdout.write(self.style.SUCCESS(
                    f'2.0: Successfully deleted a old administrator.'))
            
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
                '2.1: An error occurred while creating '
                f'a new administrator. Error: {exception}'))
        
        else: # Log action positively accomplished:
            self.stdout.write(self.style.SUCCESS(
                '2.1: Successfully created a new administrator.'))
            # Add administrator user to RedWrite group:
            self.rw_group.user_set.add(self.administrator)
            self.stdout.write(self.style.SUCCESS(
                '2.2: Successfully added Administrator to '
                'ReadWriteAccess group.'))

    def create_default_groups(self):

        def create_rw_group():
            # Check if RW group exist:
            if Group.objects.filter(name='ReadWriteAccess').exists():
                # Deled old RW group:
                Group.objects.get(name='ReadWriteAccess').delete()
                # Inform about old RW group deletion:
                self.stdout.write(self.style.WARNING(
                    f'1.0: Old RW group has been deleted.'))
            # Create a new RW group:
            return Group.objects.get_or_create(name='ReadWriteAccess')

        def create_ro_group():
            # Check if RO group exist:
            if Group.objects.filter(name='ReadOnlyAccess').exists():
                # Deled old RO group:
                Group.objects.get(name='ReadOnlyAccess').delete()
                # Inform about old RO group deletion:
                self.stdout.write(self.style.WARNING(
                    f'1.0: Old RO group has been deleted.'))
            # Create a new RO group:
            return Group.objects.get_or_create(name='ReadOnlyAccess')

        def create_rw_permission():
            # Create a new RW permission:
            return Permission.objects.filter(codename__in=[
                'read_write', 'read_only'])

        def create_ro_permission():
            # Create a new RO permission:
            return Permission.objects.filter(codename='read_only')

        try:
            # Try to make action:
            self.rw_group, rw_created = create_rw_group()
        
        except Exception as exception:
            # Log action negatively accomplished:
            self.stdout.write(self.style.WARNING(
                '1.1: An error occurred while creating '
                f'a new RW group. Error: {exception}'))
        
        else:
            # Log action positively accomplished:
            self.stdout.write(self.style.SUCCESS(
                '1.1: Successfully created RW group.'))
            
            try: # Try to make action:
                rw_permission = create_rw_permission()
            
            except Exception as exception:
                # Log action negatively accomplished:
                self.stdout.write(self.style.WARNING(
                    '1.2: An error occurred while creating '
                    f'a new RW permission. Error: {exception}'))
            
            else: # Log action positively accomplished:
                self.stdout.write(self.style.SUCCESS(
                    '1.2: Successfully created RW permission.'))
                # Assign permissions to RW group:
                self.rw_group.permissions.set(rw_permission)
            
        try:
            # Try to make action:
            self.ro_group, ro_created = create_ro_group()
        
        except Exception as exception:
            # Log action negatively accomplished:
            self.stdout.write(self.style.WARNING(
                '1.3: An error occurred while creating '
                f'a new RO group. Error: {exception}'))
        else:
            # Log action positively accomplished:
            self.stdout.write(self.style.SUCCESS(
                '1.3: Successfully created RO group.'))
            
            try:
                # Try to make action:
                ro_permission = create_ro_permission()
            
            except Exception as exception:
                # Log action negatively accomplished:
                self.stdout.write(self.style.WARNING(
                    '1.4: An error occurred while creating '
                    f'a new RO permission. Error: {exception}'))
            
            else: # Log action positively accomplished:
                self.stdout.write(self.style.SUCCESS(
                    '1.4: Successfully created RO permission.'))
                # Assign permissions to RO group:
                self.ro_group.permissions.set(ro_permission)

    def handle(self, *args, **options):
        
        # 1: Create default groups:
        self.create_default_groups() 
        # 2: Create default administrator:
        self.create_default_administrator()
