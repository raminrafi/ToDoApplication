from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=65, min_length=8, write_only=True)
    email=serializers.CharField(max_length=255, min_length=8)

    class Meta:
        model = User
        fields = ['email','password']

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            return super().validate(attrs)
        else:
            raise serializers.ValidationError({'email', ('This email doesnt exist')})

    def create(self ,validated_data):
        return User.objects.create_user(**validated_data)