from django.db import models

# Create your models here.
class Student(models.Model):
    name='Marshad'
models.CharField(max_length=100)
age=models.IntegerField()
score=models.FloatField()