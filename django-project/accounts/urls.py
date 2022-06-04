from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    RegisterView, LoginView, LogoutView, ChangePasswordView,
    CustomAuthToken
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    # database token
    path('api-token-auth/', CustomAuthToken.as_view(), name='obtain-auth-token'),
    # json Web token
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh')
]

"""
참고용
api/v1/accounts/ register/ [name='register']
api/v1/accounts/ verify-registration/ [name='verify-registration']
api/v1/accounts/ send-reset-password-link/ [name='send-reset-password-link']
api/v1/accounts/ reset-password/ [name='reset-password']
api/v1/accounts/ login/ [name='login']
api/v1/accounts/ logout/ [name='logout']
api/v1/accounts/ profile/ [name='profile']
api/v1/accounts/ change-password/ [name='change-password']
api/v1/accounts/ register-email/ [name='register-email']
api/v1/accounts/ verify-email/ [name='verify-email']
"""