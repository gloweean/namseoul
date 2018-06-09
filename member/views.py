from rest_framework.views import APIView
from rest_framework import generics, permissions, authentication
from utils.custom_permissions import ObjectIsRequestUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from .serializers.member import UserSerializer, UserCreateSerializer
from member.models import MyUser


User = get_user_model()


class UserSignUpView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = UserCreateSerializer
    

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        ObjectIsRequestUser
    )


class UserLogoutView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    
    def get(self, request):
        token = Token.objects.get(key=request._auth)
        user = User.objects.get(pk=token.user_id)
        user.auth_token.delete()
        return Response({'response': 'Logout Completed'})
