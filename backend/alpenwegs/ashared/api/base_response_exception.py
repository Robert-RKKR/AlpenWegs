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

    # Define error response dictionary:
    error_response = {}

    # Collect HTTP response:
    response = exception_handler(exc, context)

    if isinstance(response.data, dict):
        # Collect error message based od detail key:
        error_response['error_message'] = response.data.get(
            'detail', 'An error occurred.')
        # Collect response status code:
        error_response['error_status'] = response.status_code
        # Collect error code if available:
        error_response['error_code'] = response.data.get(
                'code', 'api_error')
        # Collect error details if available:
        error_response['error_details'] = response.data.get(
            'messages', [])
        
    # Return collected error response:
    return error_response, response

# Custom exception handler function: 
def base_exception_handler(
    exc: dict,
    context: dict,
) -> Response:
    """
    Base exception handler to return JSON error responses.
    """

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
            'error_details': str(exc),
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
