from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=100)
    entryText = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default="")

    def __str__(self):
        return f"{self.title}: {self.entryText}"
    