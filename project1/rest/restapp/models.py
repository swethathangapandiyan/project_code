from django.db import models
class Task(models.Model):
    task_name=models.CharField(max_length=200)
    task_desk=models.CharField(max_length=200)
    date_create=models.CharField(max_length=200)



# Create your models here.
