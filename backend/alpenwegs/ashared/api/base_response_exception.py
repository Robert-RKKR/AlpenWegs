# AlpenWegs import:
from alpenwegs.ashared.api.base_exceptions import BaseAPIException

# Rest framework import:
from rest_framework.views import exception_handler
from rest_framework.response import Response

def collect_exception_data(
    exc: dict,
    context: dict,
 ) -> dict:
    """
    Collects exception data to return a structured error response.
    """

    def collect_message(data):
        # Try to collect message from details key:
        if data.get('detail'):
            # Return collected message:
            return data['detail']
        
        # If details key is not available, return default message:
        return 'An error occurred.'

    def collect_code(data):
        # Try to collect code from code key:
        if data.get('code'):
            # Return collected code:
            return data['code']
        
        else:
            try:
                # Try to collect code from detail key:
                return data['detail'].code
            except Exception:
                pass

        # Return default code if not available:
        return 'An error occurred.'

    # Define error response dictionary:
    error_response = {}

    # Collect HTTP response:
    response = exception_handler(exc, context)

    if isinstance(response.data, dict):
        # Collect error message based od detail key:
        error_response['error_message'] = collect_message(response.data)
        # Collect error code if available:
        error_response['error_code'] = collect_code(response.data)
        # Collect response status code:
        error_response['error_status'] = response.status_code
        # Collect error details if available:
        error_response['error_details'] = response.data.get(
            'messages', [])
        
    # Return collected error response:
    return error_response, response

def base_exception_handler(
    exc: dict,
    context: dict,
) -> Response:
    """
    Base exception handler to return JSON error responses.
    """

    error_response, response = collect_exception_data(
        context=context,
        exc=exc,
    )
    return Response(
        data=error_response,
        status=response.status_code
    )

    try:
        # Try to collect exception data:
        error_response, response = collect_exception_data(
            context=context,
            exc=exc,
        )

    except Exception as exception:
        # If response if not available, raise 500 error:
        error_response = {
            'error_code': 500,
            'error_message': 'Internal Server Error',
            'error_details': str(exception),
        }

        # Return error response:
        return Response(
            data=error_response,
            status=500
        )

    else:
        # Return error response:
        return Response(
            data=error_response,
            status=response.status_code
        )
