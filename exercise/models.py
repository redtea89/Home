from django.db import models

# Create your models here.
class Exercise(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=100, default='', blank=True)
    status = models.CharField(max_length=20, default='시작', blank=True)
    created = models.DateTimeField(auto_now_add=True)