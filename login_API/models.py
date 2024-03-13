from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
from predefined_exercises.models import Exercise, Goal
from django.contrib.auth.models import User


class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workout_plans")
    workout_frequency = models.PositiveIntegerField()
    daily_session_duration = models.PositiveBigIntegerField()
    goals = models.ManyToManyField(Goal)
    exercises = models.ManyToManyField(Exercise, through="PlannedExercise")

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    workout_plans = models.ManyToManyField(WorkoutPlan)

class PlannedExercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    repetitions = models.IntegerField()
    sets = models.IntegerField()
    duration = models.DurationField(null=True, blank=True)
    distance = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    

