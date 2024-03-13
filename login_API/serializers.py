from rest_framework import serializers
from .models import User, WorkoutPlan,PlannedExercise,WorkoutPlan
from predefined_exercises.models import Exercise 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data["password"]
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PlannedExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlannedExercise
        fields = ['exercise', 'workout_plan', 'repetitions', 'sets', 'duration', 'distance']

class WorkoutPlanSerializer(serializers.ModelSerializer):
    exercises = PlannedExerciseSerializer(many=True)
    class Meta:
        model = WorkoutPlan
        fields = ['workout_frequency', 'daily_session_duration','goals', 'exercises']

    def create(self, validated_data):

        request = self.context.get("request")
        validated_data["user"] = request.user
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        exercises_data = validated_data.pop("exercises")
        for exercise_data in exercises_data:
            print(exercise_data)
        return super().update(instance,validated_data)