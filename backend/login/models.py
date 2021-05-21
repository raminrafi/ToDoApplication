from django.db import models

class login(models.Model):
    Email = models.EmailField(max_length=140)
    Password = models.CharField(max_length=140)

    class Meta:
     ordering = ['User_name']
# Create your models here.
