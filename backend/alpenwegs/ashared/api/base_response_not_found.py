# Rest framework import:
from django.http import JsonResponse

def base_page_not_found(
    request,
    exception,
):
    
    # Return custom 404 JSON response:
    return JsonResponse(
        {
            'page_status': False,
            'page_data': None,
            'page_error': {
                'error_message': 'The requested API endpoint was not found.',
                'error_code': 'not_found',
                'error_status': 404,
                'error_details': []
            },
        },
        status=404,
    )
