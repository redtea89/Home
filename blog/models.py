from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    text = models.TextField()
    tag = models.CharField(max_length=30, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField(null=True)


# class Image(models.Model):
#     title = models.CharField(max_length=100)
#     subtitle = models.CharField(max_length=100)
#     text = models.TextField()
