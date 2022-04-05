from django.urls import path
from . import views

urlpatterns = [
    # path('', views.shelter, name='shelter'),
    path('', views.ShelterView.as_view(), name='shelter'),
    path('listview/', views.ShelterListView.as_view()),
    path('detailview/<int:pk>', views.ShelterDetailView.as_view()),
    path('region/<str:region>/', views.region_shelter, name='region_shelter'),
    path('detail/<int:shelter_id>', views.detail_shelter, name='detail_shelter'),
    path('upload/upload/', views.upload, name='shelter_upload'),
    # path('<int:shelter_id>/', views.manage_shelter, name='manage_shelter'),
    # path('<int:shelter_id>/update', views.update_shelter, name='update_shelter'),
]
