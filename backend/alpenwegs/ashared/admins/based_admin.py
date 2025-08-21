# Django import:
from django.core.serializers import serialize
from django.http import HttpResponse
from django.contrib import messages
from django.contrib import admin

# Python import:
from datetime import datetime
import json
import csv
import re

# Constants:
KEY_TO_FILTER = [
    'is_root',
    'is_deleted',
    'ico'
]

# Helper function:
def collect_keys(queryset):
    """
    Collect model keys.
    """

    for query_object in queryset:
        try: # Try to collect model keys:
            raw_data = serialize('json', [query_object],
                use_natural_foreign_keys=True, use_natural_primary_keys=True)
            dict_data = json.loads(raw_data)[0]['fields']
            keys = list(dict_data.keys())
        except: # Return an empty list on failure:
            return []
        else:
            # Filter key:
            return_key = []
            for key in keys:
                if not key in KEY_TO_FILTER:
                    return_key.append(key)
            # Return filtered keys:
            return return_key


# Base admin class:
class BaseAdmin(admin.ModelAdmin):
    """
    Base Admin model.
    """

    actions = [
        'make_nonactive',
        'make_active',
        'export_objects'
    ]
    
    @admin.action(description='Export to CSV')
    def export_objects(self, request, queryset):
        """
        Export object/s to csv format with human-readable dates.
        """

        # Helper function:
        def transform_value(value):
            """
            Apply various transformations to a object value.
            """
            # Format datetime values:
            if isinstance(value, datetime):
                return value.strftime('%Y-%m-%d %H:%M:%S')
            # Convert boolean True to 'True':
            if value is True:
                return 'True'
            # Convert boolean False to 'False':
            if value is False:
                return 'False'
            # Return transformed value:
            return value

        # Collect object representation:
        model_repr = self.model_representation()
        # Collect current data time for file name:
        current_date = datetime.now().strftime("%Y-%m-%d %H-%M")
        # Create a new filename:
        filename = f'{model_repr} - {current_date}.csv'
        
        # Prepare HTTP response with csv file:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        writer = csv.writer(response, delimiter=';')
        
        # Get field names and their verbose names:
        field_verbose_names = self.get_field_verbose_names(queryset.model)
        field_names = [name for name, verbose_name in field_verbose_names]
        verbose_names = [verbose_name.title() for name,
            verbose_name in field_verbose_names]
        # Save field names to csv file:
        writer.writerow(verbose_names)
        # Prepare object data:
        query_objects = queryset.values_list(*field_names)
        for query_object in query_objects:
            human_readable_row = [transform_value(value) for value in query_object]
            writer.writerow(human_readable_row)

        # Return HTML response containing csv file:
        return response
    
    @admin.action(description='Make object nonactive')
    def make_nonactive(self, request, queryset):
        """
        Mark object/s as not active.
        """
        
        # Update object is active value:
        updated = queryset.update(is_active=False)
        # Collect object representation:
        model_repr = self.model_representation()
        # Send message:
        self.message_user(request,
            f'{updated} {model_repr} was successfully marked as not active.',
            messages.SUCCESS)

    @admin.action(description='Make object active')
    def make_active(self, request, queryset):
        """
        Mark object/s as active.
        """

        # Update object is active value:
        updated = queryset.update(is_active=True)
        # Collect object representation:
        model_repr = self.model_representation()
        # Send message:
        self.message_user(request,
            f'{updated} {model_repr} was successfully marked as active.',
            messages.SUCCESS)

    # Additional class methods:
    def camel_case_to_spaces(self, name):
        """
        Convert camel case to space-separated words.
        """

        return re.sub(r'(?<!^)(?=[A-Z])', ' ', name).replace('_', ' ')
    
    def model_representation(self):
        """
        Return model string representation.
        """

        return self.camel_case_to_spaces(self.__class__.__name__)
    
    def get_field_verbose_names(self, model):
        """
        Get verbose names for each field in the model,
        excluding keys in KEY_TO_FILTER.
        """

        fields = model._meta.fields
        field_verbose_names = [
            (field.name, field.verbose_name) for field in fields
            if field.name not in KEY_TO_FILTER]
        return field_verbose_names
