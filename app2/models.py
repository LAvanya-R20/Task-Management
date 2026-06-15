from django.db import models

# Create your models here.

class register1(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
