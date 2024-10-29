from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    description = models.TextField()
    deadline = models.DateField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
