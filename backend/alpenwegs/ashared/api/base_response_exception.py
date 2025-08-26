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

    print(f'Exception response: {response}')
    print(f'Exception response.status_code: {response.status_code}')
    print(f'Exception response.data: {response.data}')
    
    # Check collected response:
    if response:
        # Prepare error response to return:
        page_errors = []
        
        try:
            # Collect error message from response:
            error = {
                'error_code': response.status_code,
                'error_message': response.data['detail']
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

        return exc

        # If response if not available, raise 500 error:
        error = {
            'error_code': 500,
            'error_message': 'Internal Server Error',
            'debug': str(exc),
        }
        
        # Return error response:
        return Response(error, status=500)
