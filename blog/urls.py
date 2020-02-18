"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView

admin.site.site_header = 'Plain-Blog Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('api/blog/', include('blogging_api.urls')),

    # / routes to index.html
    url(r'^$', serve,
        kwargs={'path': 'index.html'}),
    # static files (*.css, *.js, *.jpg etc.) served on /
    url(r'^(?!/static/.*)(?P<path>.*\..*)$',
        RedirectView.as_view(url='/static/%(path)s')),
]
