from datetime import timezone, timedelta

from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300)
    publication_date = models.DateField('published')
    content = models.TextField()
    content_short = models.TextField(default='')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.publication_date >= timezone.now() - timedelta(days=30)

    def get_short_json(self):
        return {
            'title': self.title,
            'id': self.pk,
            'publication_date': self.publication_date,
            'content_short': self.content_short
        }

    def get_json(self):
        return {
            'title': self.title,
            'id': self.pk,
            'publication_date': self.publication_date,
            'content': self.content,
            'content_short': self.content_short
        }
