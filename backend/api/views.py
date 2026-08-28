from django.shortcuts import render

from .serializer import ApplicationSerializer, InterviewSerializer
from rest_framework import viewsets
from .models import Application, Interview
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    # Override get_queryset to filter applications by the logged-in user
    def get_queryset(self):
        user = self.request.user
        return Application.objects.filter(user=user)

    # Override perform_create to associate the logged-in user with the created application
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Interview.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
