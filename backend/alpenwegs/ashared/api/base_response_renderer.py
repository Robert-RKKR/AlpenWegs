# Rest framework import:
from rest_framework.renderers import JSONRenderer


# Custom response handler: 
class BaseResponseRenderer(JSONRenderer):
    """
    Define base API response renderer for AlpenWegs API.
    
    This renderer will handle the response structure
    and will be used for all API responses.
    """

    def render(self,
        data: dict,
        accepted_media_type: bool = None,
        renderer_context: dict = None
    ) -> str:

        # Get the response from renderer context:
        response = renderer_context.get('response', None)

        # Check if response is successful:
        success = response and 200 <= response.status_code < 400

        # Define the response structure:
        response_data = {
            'page_status': success,
            'page_data': None,
            'page_errors': None,
        }

        # Check if response is successful:
        if success:
            
            # If response is successful, check if data are paginated:
            if isinstance(data, dict) and 'results' in data and 'count' in data:
                
                # Prepare paginated response:
                response_data['page_data'] = {
                    'count': data.get('count'),
                    'next': data.get('next'),
                    'previous': data.get('previous'),
                    'items': data.get('results'),
                }
            
            else:
                # Add data response directly:
                response_data['page_data'] = data
        
        else:
            # If response is not successful, add errors to response:
            response_data['page_errors'] = data

        # Return the rendered response as original method:
        return super().render(
            accepted_media_type=accepted_media_type,
            renderer_context=renderer_context,
            data=response_data,
        )
