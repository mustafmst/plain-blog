from django.db import models
from rest_framework import serializers


class Tag(models.Model):
    """
    Post tag model
    """
    name = models.CharField(max_length=50, unique=True, primary_key=True)

    def __str__(self):
        return self.name


class TagSerializer(serializers.Serializer):
    """
    REST API serializer for Tag model
    """
    name = serializers.CharField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        return Tag.objects.create(**validated_data)
