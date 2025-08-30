# AlpenWegs import:
from alpenwegs.ashared.constants.action_type import ActionTypeChoices
from alpenwegs.ashared.models.base_model import BaseModel
from alpenwegs.logger import api_logger as logger

# AlpenWegs application import:
from notifications.object_collector import collect_object_data
from notifications.notification import Notification
from profiles.models.user_model import UserModel
from notifications.changer import log_change

# Django import:
from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import ErrorDetail
from rest_framework.response import Response
from rest_framework import status


# Base Mixin class:
class BaseMixin():

    def _create_notification(self,
        instance: BaseModel,
        action: ActionTypeChoices,
        user: UserModel,
        serializer = False,
        log_changes = False
    ) -> None:
        """
        Create a notification for object changes.
        """

        if log_changes:
            # Create a new change notification:
            log_change(
                instance=instance,
                user=user,
                action=action,
            )
            
            # Collect object data:
            object_related_data = collect_object_data(instance)
            model_name = object_related_data.get('model_name', False)
            instance_representation = object_related_data.get(
                'object_representation', False)
            # Collect url:
            url = serializer.data.get('url') if serializer else None

            # Collect action representation:
            action_repr = ActionTypeChoices.value_from_int(action)

            # Create a new notification:
            notification = Notification(
                task_id=f'api-{action_repr}',
                channel_name=f'user_{user.id}',
            )
            # Send notification:
            notification.info(f'{model_name} "{instance_representation}" '
                f'has been {action_repr}d.', url=url
            )






    def format_validation_error(self,
        error_obj: ValidationError) -> dict:
        """
        Format create validation error data.
        """

        formatted_errors = {}
        # Iterate thru all returned validator errors:
        for field, error_list in error_obj.detail.items():
            
            # Check if it's a list of ErrorDetail objects:
            if isinstance(error_list, list) and all(isinstance(
                err, ErrorDetail) for err in error_list):
                formatted_errors[field] = {
                    # Get the message from the first ErrorDetail:
                    "message": str(error_list[0]),
                    # Get the code from the first ErrorDetail:
                    "code": error_list[0].code}
            
            else: # Return not formatted error list:
                formatted_errors[field] = str(error_list)
        
        return {'error_parameters': formatted_errors}

    def _root_object_verification(self,
        instance: object) -> bool:
        """
        Check if an instance is not a root object.
        """

        # Collect is_root attribute:
        is_root = getattr(instance, 'is_root', True)
        # If root object attribute is True return API error:
        if is_root:
            # Prepare Root error message:
            message = f"Object {instance} can't be changed, "\
                "because it's a root object"
            
            # Prepare error response:
            return self._return_api_error(
                status.HTTP_403_FORBIDDEN,
                'PermissionDenied',
                message,
                {'error_type': 'RootProtectedError'})
        
        # If object is not a root object, return False value:
        return False










































    def _return_api_response(self,
        page_status: int,
        page_data: str,
        page_headers: bool = False,
        page_message: str = False) -> Response:
        """
        Create API response - Standard.
        """

        # Prepare response:
        response_data = {
            'page_status': True,
            'page_results': page_data}
        
        # Check if page message ned to be added:
        if page_message:
            response_data['page_message'] = page_message
        
        # Return created API response:
        if page_headers:
            # Prepare headers:
            page_headers = self.get_success_headers(page_data)
            return Response({
                'page_status': True,
                'page_results': page_data},
                page_status, headers=page_headers)
        
        else: # Return response without headers:
            return Response({
                'page_status': True,
                'page_results': page_data}, page_status)

    def _return_api_error(self,
        error_code: int,
        error_type: str,
        error_message: str,
        additional_data: dict = None) -> Response:
        """
        Create API response - Error.
        """

        # Prepare API error value:
        api_error = {
            'error_code': error_code,
            'error_type': error_type,
            'error_message': error_message}
        
        # Check if additional data ned to be added:
        if isinstance(additional_data, dict):
            api_error.update(additional_data)
        
        # Return created API response:
        return Response({
            'page_status': False,
            'page_errors': [api_error]}, error_code)


    def _log_api_call(self,
        request,
        is_error_message = False,
        error_code = None) -> None:
        """
        Log all API calls.
        """

        # Collect request data:
        request_method = request.method
        request_user = request.user
        request_path = request.path
        collected_data = {
            'session': request.session,
            'method': request_method,
            'auth': request.auth,
            'path': request_path,
            'code': error_code
        }
        
        # Create message for a new log:
        if is_error_message:
            # Create a new log entry:
            logger.warning(message)
        
        else: # Create a new positive negative message:
            message = f'{request_method} API call to '\
                f'"{request_path}" was successfully made.'
            # Create a new log:
            logger.debug(message)
