from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
class Vacation(models.Model): #This is the vacation model with fields as required by the exercise.
    description = models.CharField(max_length=300, default="none")
    start_date = models.DateField(default=datetime.datetime.now)
    end_date = models.DateField(default=datetime.datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vacation")
    def __str__(self):
        return self.description
#complete = models.BooleanField()