# Rest framework import:
from rest_framework.views import exception_handler
from rest_framework.response import Response

# Custom exception handler function: 
def base_exception_handler(
    exc,
    context
) -> Response:
    """
    Base exception handler to return JSON error responses.
    """

    # Collect HTTP response:
    response = exception_handler(exc, context)
    
    # Check collected response:
    if response:
        # Prepare error response to return:
        page_errors = []
        
        try:
            # Collect error message from response:
            error = {
                'error_code': response.status_code,
                'error_message': response.data
            }
            # Add error message to response:
            page_errors.append(error)
        
        except:
            # If error message is not available collect response:
            error = {
                'error_message': str(response)
            }
            # Add error message to response:
            page_errors.append(error)
        
        # Return error response:
        return Response(page_errors, status=response.status_code)
    
    else:
        # If response if not available, raise exception:
        raise InterruptedError(exc)
