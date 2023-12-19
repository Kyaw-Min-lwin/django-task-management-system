from django.db import models
from datetime import datetime


# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=10000)
    time = models.DateTimeField(default=datetime.now)
