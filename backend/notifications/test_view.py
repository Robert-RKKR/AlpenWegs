# api.py
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from notifications.notification import Notification

class NotifyMeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        name = user.get_full_name() or user.username or "there"

        svc = Notification(
            task_id="hello-user",
            channel_name=f"user_{user.id}",
        )
        svc.info(message=f"Hello {name}!", url="/profile/")

        return Response({"status": "ok", "message": f"Sent to user_{user.id}"})
