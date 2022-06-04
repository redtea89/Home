from django.urls import path
from .views import (
    PostListCreateView, PostRetrieveUpdateDeleteView
)

urlpatterns = [
    path('posts', PostListCreateView.as_view(), name='index-list'),
    path('posts/<int:pk>', PostRetrieveUpdateDeleteView.as_view(), name='index-detail')
]