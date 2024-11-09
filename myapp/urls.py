from django.urls import path, include
from . import views
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register('exercises', views.ExerciseViewSet)

urlpatterns = [
    path('', views.getExercises, name='exercises'),
    path('add/', views.add_Exercise, name='add_exercise'),
    # path('rest-api/', include(router.urls)),
    path('auth/', include('rest_framework.urls'), name='rest_framework'),
]