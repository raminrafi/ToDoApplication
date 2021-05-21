from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework import serializers
from .models import registration


class registrationserializer(serializers.ModelSerializer):
    class Meta:
        model = registration
        fields = ['User_name', 'Email', 'Password','Cpassword']