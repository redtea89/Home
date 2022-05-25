from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.PostListCreatetView.as_view(), name='index-list'),
    path('posts/<int:pk>', views.PostRetrieveUpdateDeleteView.as_view(), name='index-detail')
]