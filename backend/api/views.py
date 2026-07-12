from django.shortcuts import render

from backend.api.serializer import ApplicationSerializer, InterviewSerializer
from rest_framework import viewsets
from .models import Application, Interview

# Create your views here.
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer