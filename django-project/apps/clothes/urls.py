from django.urls import path
from . import views


urlpatterns = [
    path('kinds', views.ClothesListCreateView.as_view(), name='clothes-list'),
    path('kinds/<int:pk>', views.ClothesRetrieveUpdateDeleteView.as_view(), name='clothes-detail'),
    path('suggetion', views.SuggetionView.as_view(), name='suggetion-view'),
]