# Rest framework import:
from rest_framework.views import exception_handler
from rest_framework.response import Response

# Custom exception handler function: 
def custom_exception_handler(exc, context):
    """
    Custom exception handler to return JSON responses.
    """

    # Collect HTTP response:
    response = exception_handler(exc, context)
    
    # Check collected response:
    if response:
        # Prepare error response to return:
        error_response = {
            'page_status': False,
            'page_errors': []}
        
        # Try to collect response data:
        try:
            error = {'error_code': response.status_code,
                'error_message': response.data}
            error_response['page_errors'].append(error)
        
        # If not available return response:
        except:
            error = {'error_message': str(response)}
            error_response['page_errors'].append(error)
        
        # Return error response:
        return Response(error_response, status=response.status_code)
    
    else: # If response if not available, raise exception:
        raise InterruptedError(exc)
