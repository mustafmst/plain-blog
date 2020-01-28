from django.urls import path

from . import views

urlpatterns = [
    path('', views.names),
    path('posts', views.all_posts)
]
