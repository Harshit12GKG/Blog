"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import re_path as url
from django.views.static import serve

urlpatterns = [
    path('site-administration/login/', admin.site.urls),
    path('', include('home.urls')),
    path('api/', include('home.urls_api')),
    path('api-auth/', include('rest_framework.urls')),
    path('froala_editor/', include('froala_editor.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':
    settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root':
    settings.STATIC_ROOT}),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root =  settings.MEDIA_ROOT)

admin.site.site_header = "Blogsz Admin Portal"
admin.site.site_title = "Blogsz Admin Portal"
admin.site.index_title = "Welcome to Blogsz Admin Portal"