from django.http import JsonResponse
from django.shortcuts import render


def names(request):
    return JsonResponse({'names': ['William', 'Rod', 'Grant']})
