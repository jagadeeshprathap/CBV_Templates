from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=12)