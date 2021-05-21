from django.db import models
from django import forms
# Create your models here.

class registration(models.Model):
    User_name = models.CharField(max_length=140)
    Email = models.EmailField(max_length=140)
    Password = models.CharField(max_length=140)
    Cpassword = models.CharField(max_length=140)

    class Meta:
     ordering = ['User_name']
