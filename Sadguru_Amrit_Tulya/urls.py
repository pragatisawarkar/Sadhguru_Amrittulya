"""Sadguru_Amrit_Tulya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from item.views import welcome, item_details, add_item, remove_item
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', welcome, name='welcome'),
    url('add/', add_item),
    url(r'remove/(?P<id>\d+)/$', remove_item),
    url(r'details/(?P<id>\d+)/$', item_details),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

