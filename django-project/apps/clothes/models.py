from django.db import models


class Clothes(models.Model):
    category = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    bought = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    

class History(models.Model):
    clothes = models.ManyToManyField(Clothes)
    wearing = models.IntegerField(default=1)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
    
    
