from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.response import Response


User = get_user_model()


class UserLogoutView(APIView):
    def get(self, request):
        token = Token.objects.get(key=request._auth)
        user = User.objects.get(pk=token.user_id)
        user.auth_token.delete()
        return Response({'response': 'Logout Completed'})
