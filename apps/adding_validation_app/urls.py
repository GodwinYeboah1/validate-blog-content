from django.conf.urls import url, include
from django.contrib import admin 

from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^blogs$', views.home),
    url(r'^blog/new$', views.create_blog),
    url(r'^blog/edit/(?P<id>\d+)$', views.update_page),
    url(r'^blog/edits/(?P<id>\d+)$', views.update),
    url(r'^blog/destory/(?P<id>\d+)$', views.destory)

]
