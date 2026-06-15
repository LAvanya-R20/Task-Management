from django.db import models

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ('assigned', 'Assigned'),
        ('ongoing', 'Ongoing'),
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    person = models.CharField(max_length=100)
    email = models.EmailField()
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

class TaskHistory(models.Model):
    STATUS_CHOICES = [
        ('assigned', 'Assigned'),
        ('ongoing', 'Ongoing'),
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    person = models.CharField(max_length=100)
    email = models.EmailField()
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)