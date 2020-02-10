import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response

from blogging_api.models.post import Post, PostSerializer


@api_view(['GET'])
def all_posts(request):
    """
    Get all blog posts
    :param request:
    :return: all blog posts in json format
    """
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    logging.debug(posts)
    logging.debug(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
def get_post(request, id):
    """
    Get single blog post
    :param request:
    :param id: id of a blog post
    :return: blog post in json format
    """
    post = Post.objects.get(pk=id)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)
