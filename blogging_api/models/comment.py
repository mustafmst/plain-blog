from django.db import models

from blogging_api.models.post import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    content = models.TextField(max_length=250)
