from django.db import models
from django import forms
# Create your models here.

class task(models.Model):
    title = models.CharField(max_length=140)
    label = models.EmailField(max_length=140)
    priority = models.CharField(max_length=140)

    class Meta:
     ordering = ['title']
