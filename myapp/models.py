from django.db import models

# Create your models here.

class Exercises(models.Model):
    name = models.CharField(max_length=225)

class MuscleGroup(models.Model):
    name = models.CharField(max_length=225)

class ExerciseMusclegroup(models.Model):
    exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE, related_name='muscle_groups')
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE, related_name='exercises')
    
    class Meta:
        unique_together = ['exercise', 'muscle_group']

class ExerciseLog(models.Model):
    exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE, related_name='logs')
    date = models.DateField()
    weight = models.IntegerField(help_text="weights used")
    set_count = models.IntegerField(help_text="No. of sets completed")
