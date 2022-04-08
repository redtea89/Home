"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
import blog.urls, game.urls, shelter.urls, accounts.urls, \
    exercise.urls, apis.urls

from blog import views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


router = routers.DefaultRouter()
router.register(r'blogs', views.BlogViewSet)

urlpatterns = [
    path('manage/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='api')),
    path('api', include(router.urls)),
    path('', include(blog.urls)),
    path('game/', include(game.urls)),
    path('shelter/', include(shelter.urls)),
    path('accounts/', include(accounts.urls)),
    path('registration/', include('django.contrib.auth.urls')),
    path('exercise/', include(exercise.urls)),
    path('apis/', include(apis.urls)),
]
 