from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import (
    RegisterAPI,
    LoginAPI,
    UserView,
    CreateWorkoutAPI,
    UserView,
    UpdateWorkoutAPI
)

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('user/', UserView.as_view(), name='user'),
    path('create/', CreateWorkoutAPI.as_view(), name='create_workout'),
    path('update/<int:pk>/', UpdateWorkoutAPI.as_view(), name='update_workout_api'),
    path("profile/<int:pk>/", UserView.as_view()),
]
