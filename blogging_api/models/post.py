from datetime import timezone, timedelta

from ckeditor.fields import RichTextField
from rest_framework import serializers
from django.db import models


class Post(models.Model):
    """
    Stores single blog post. Content preferably in markdown.
    """
    title = models.CharField(max_length=150)
    publication_date = models.DateField('published')
    content = RichTextField()
    content_short = models.TextField(default='', max_length=500)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.publication_date >= timezone.now() - timedelta(days=30)


class PostSerializer(serializers.Serializer):
    """
    REST API serializer for Post model
    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    publication_date = serializers.DateField()
    content = serializers.CharField()
    content_short = serializers.CharField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.content_short = validated_data.get('content_short', instance.content_short)
