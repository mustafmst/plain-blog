from datetime import timezone, timedelta

from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300)
    publication_date = models.DateField('published')
    content = models.TextField()

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.publication_date >= timezone.now() - timedelta(days=30)
