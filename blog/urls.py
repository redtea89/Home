from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:textId>/', views.blog, name='blogDetail'),
]
