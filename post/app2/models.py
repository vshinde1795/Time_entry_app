from django.db import models

# Create your models here.
class TaskData(models.Model):
    task = models.CharField(max_length=255)
    project = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    stop_time = models.CharField(max_length=100)
    total_time = models.CharField(max_length=100)




