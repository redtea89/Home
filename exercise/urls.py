from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/exercise/', views.exercise_list, name='exercise_api'),
    path('exercise/', views.ExerciseView.as_view(), name='exercise'),
]
#don't necessarily,but it gives a simple way of referring to a specific format.
urlpatterns = format_suffix_patterns(urlpatterns)
