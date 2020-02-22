from django.urls import path

from blogging_api.views.post import all_posts, get_post, get_homepage_content, get_infopage_content

urlpatterns = [
    path('posts', all_posts),
    path('posts/<int:id>', get_post),
    path('posts/homepage', get_homepage_content),
    path('posts/infopage', get_infopage_content),
]
