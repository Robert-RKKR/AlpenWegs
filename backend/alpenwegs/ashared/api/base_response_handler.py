# Rest framework import:
from rest_framework.views import exception_handler
from rest_framework.response import Response

# Custom response handler function: 
def base_response_handler(exc, context):
    """
    Custom API response.
    """

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context.get('response', None)

        # Default structure:
        response_data = {
            'page_status': True if response and 200 <= response.status_code < 400 else False,
            'page_data': data if response and 200 <= response.status_code < 400 else None,
            'page_errors': [] if response and 200 <= response.status_code < 400 else data,
        }

        return super().render(response_data, accepted_media_type, renderer_context)
