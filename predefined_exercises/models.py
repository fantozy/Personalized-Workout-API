from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    instructions = models.TextField()
    muscles = models.ManyToManyField("Muscle",blank=True)
    difficulty_level = models.CharField(max_length=50)
    goal = models.ForeignKey("goal", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Muscle(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Goal(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name