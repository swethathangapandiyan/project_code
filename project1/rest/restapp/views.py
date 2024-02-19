from django.shortcuts import render
from serializers import TaskSerializers
from rest_framework import viewsets
from .models import Task

class TaskViewSet(viewsets.ModelViewSet):
    queryset=TaskObjects.all().order_by('-date_create')
    serializer_class = TaskSerializers



