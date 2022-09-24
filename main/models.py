from re import T
from time import time, timezone
from django.db.models.deletion import CASCADE
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Exercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="exercise", null=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workout", null=True)
    date = models.DateField(default=now, editable=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveSmallIntegerField(validators=[MaxValueValidator(9999), MinValueValidator(1)])
    reps = models.PositiveSmallIntegerField(validators=[MaxValueValidator(9999), MinValueValidator(1)])
    weight = models.PositiveSmallIntegerField(validators=[MaxValueValidator(9999), MinValueValidator(1)])
    comment = models.TextField(default="None", max_length=300)

    def __str__(self):
        return str(self.pk)