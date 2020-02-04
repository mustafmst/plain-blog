from django.urls import path

from blogging_api.views.post import all_posts, get_post

urlpatterns = [
    path('posts', all_posts),
    path('posts/<int:id>', get_post)
]
