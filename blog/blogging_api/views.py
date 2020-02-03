from django.http import JsonResponse, HttpResponse

from .models import Post


def all_posts(request):
    posts = [p.get_short_json() for p in Post.objects.all()]
    posts.sort(key=lambda x: x['publication_date'], reverse=True)
    return JsonResponse(posts, safe=False)
