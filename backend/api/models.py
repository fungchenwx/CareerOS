from django.db import models

# Create your models here.
class Application(models.Model):
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    date = models.DateField()

class Interview(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)

