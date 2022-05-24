from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.IndexListView.as_view(), name='index-list'),
    path('', views.IndexDetailView.as_view(), name='index-detail')
]