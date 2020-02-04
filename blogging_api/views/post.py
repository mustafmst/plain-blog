from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET

from blogging_api.models.post import Post


@require_GET
def all_posts(request):
    posts = [p.get_short_json() for p in Post.objects.all()]
    posts.sort(key=lambda x: x['publication_date'], reverse=True)
    return JsonResponse(posts, safe=False)


@require_GET
def get_post(request, id):
    pass
