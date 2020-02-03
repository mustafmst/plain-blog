import os

from django.apps import AppConfig


class BloggingApiConfig(AppConfig):
    name = 'blogging_api'
    urls = os.path.join(name, 'urls')
