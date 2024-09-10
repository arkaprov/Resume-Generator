from django.db import models

# Create your models here.

from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    achievements= models.TextField()
    skills = models.CharField(max_length=200)
    workExp = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=19)
    projects=models.TextField()