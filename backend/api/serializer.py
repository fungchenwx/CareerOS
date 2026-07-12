from rest_framework import serializers
from .models import Application, Interview


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["id", "company", "position", "status", "date"]

class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ["id", "application", "date", "time", "location", "notes"]

