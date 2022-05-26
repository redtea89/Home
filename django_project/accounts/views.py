from django.contrib.auth import authenticate, get_user_model, login, logout

from rest_framework import status
from rest_framework import exceptions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import RegisterSerializer

User = get_user_model()


class RegisterView(CreateAPIView):
    queryset = User
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message":"register OK"}, status=status.HTTP_201_CREATED, headers=headers)
    

class LoginView(APIView):

    def post(self, request, format=None):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return Response({"message":"login OK"}, status=status.HTTP_200_OK)
        return Response({"message":"login error"}, status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        logout(request)
        return Response({"message":"logout OK"}, status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        try:
            user = User.objects.get(username=request.user)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        password = request.data.get('password', None)
        if password is not None:
            user.set_password(password)
            user.save()
            return Response({"message":"password change OK"}, status=status.HTTP_200_OK)
        return Response({"message":"password change error"}, status=status.HTTP_400_BAD_REQUEST)


class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })