from django.contrib import admin

from .models import WorkoutPlan, PlannedExercise, UserProfile


admin.site.register(WorkoutPlan)
admin.site.register(PlannedExercise)
admin.site.register(UserProfile)