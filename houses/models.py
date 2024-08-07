from django.db import models

# Create your models here.
class House(models.Model):
  

  """Model Definition for Houses"""
  
  name = models.models.CharField(max_length=140)
  price = models.models.PositiveIntegerField()
  description = models.TextField()
  address = models.CharField(max_length=140)