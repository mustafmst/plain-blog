from django.contrib import admin

from blogging_api.models.comment import Comment
from blogging_api.models.post import Post
from blogging_api.models.tag import Tag

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
