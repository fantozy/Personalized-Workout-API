from datetime import timedelta
from django.contrib.auth import authenticate
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions
from .models import User, PlannedExercise, WorkoutPlan
from predefined_exercises.models import Exercise
from .serializers import UserSerializer, PlannedExerciseSerializer, WorkoutPlanSerializer
from .services.jwt import get_tokens_for_user
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class RegisterAPI(APIView):
    """
    API endpoint for user registration.
    """
    def post(self, request):
        """
        POST request to create a new user.

        Returns:
        - 201 Created: User successfully created.
        - 400 Bad Request: Invalid data provided.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(APIView):
    """
    API endpoint for user login.
    """
    def post(self, request):
        """
        POST request to authenticate a user and generate an access token.

        Returns:
        - Access token if authentication is successful.
        - 401 Unauthorized: Authentication failed.
        """
        name = request.data['username']
        password = request.data['password']
        user = authenticate(username=name, password=password)

        if user is None:
            raise exceptions.AuthenticationFailed("User not found")
        token = get_tokens_for_user(user)

        return Response(token)


class UserView(APIView):
    """
    API endpoint to retrieve user details.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """
        GET request to retrieve user details.

        Returns:
        - User details.
        """
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(instance=user)
        return Response(serializer.data)


class CreateWorkoutAPI(APIView):
    """
    API endpoint to create a new workout plan.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        POST request to create a new workout plan.

        Returns:
        - 201 Created: Workout plan successfully created.
        - 400 Bad Request: Invalid data provided.
        """
        serializer = WorkoutPlanSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            workout_plan = serializer.save()
            exercises_data = request.data.get("exercises", [])
            for exercise_data in exercises_data:
                exercise_id = exercise_data.get('exercise', None)
                if exercise_id:
                    try:
                        exercise_instance = Exercise.objects.get(pk=exercise_id)
                    except Exercise.DoesNotExist:
                        raise Http404("Exercise does not exist")
                else:
                    raise serializer.ValidationError("Exercise ID is required")

                PlannedExercise.objects.create(
                    exercise=exercise_instance,
                    workout_plan=workout_plan,
                    repetitions=exercise_data["repetitions"],
                    sets=exercise_data["sets"],
                    duration=timedelta(minutes=exercise_data["duration"]),
                    distance=exercise_data["distance"]
                )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateWorkoutAPI(RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update, or delete a workout plan.
    """
    permission_classes = [IsAuthenticated]
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
