# Rest framework import:
from rest_framework.renderers import JSONRenderer


# Custom response handler: 
class BaseResponseRenderer(JSONRenderer):
    """
    Custom renderer to wrap ALL API responses in the same structure.
    Supports normal data and paginated responses.
    """

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context.get('response', None)

        success = response and 200 <= response.status_code < 400

        # Default container
        response_data = {
            'page_status': success,
            'page_data': None,
            'page_errors': [],
        }

        if success:
            if isinstance(data, dict) and 'results' in data and 'count' in data:
                # Paginated response
                response_data['page_data'] = {
                    'count': data.get('count'),
                    'next': data.get('next'),
                    'previous': data.get('previous'),
                    'items': data.get('results'),
                }
            else:
                # Normal success data
                response_data['page_data'] = data
        else:
            # Error response
            response_data = data

        return super().render(response_data, accepted_media_type, renderer_context)
