from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birthday = models.DateField()
    education = models.TextField()
    skills = models.TextField()
    social = models.CharField(max_length=500)
    tags = models.CharField(max_length=300)