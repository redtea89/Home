from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Shelter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100,null=True)
    address2 = models.CharField(max_length=100,null=True)
    people = models.IntegerField(null=True)
    xplot = models.FloatField(null=True)
    yplot = models.FloatField(null=True)
    pet = models.BooleanField(default=False, null=True)
    toilet = models.PositiveSmallIntegerField(null=True)
    
    def __str__(self):
        return self.name