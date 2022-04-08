from django.db import models

# Create your models here.
class Chinese(models.Model):
    word = models.CharField(max_length=20)
    