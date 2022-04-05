from django.urls import path
from . import views

urlpatterns = [
    # path('', views.exercise, name='exercise'),
    path('', views.ExerciseView.as_view(template_name = "exercise/exercise.html"), name="exercise"),
]
