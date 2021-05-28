from rest_framework import serializers

from rest_framework import serializers
from .models import task


class taskserializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ['title', 'label', 'priority']