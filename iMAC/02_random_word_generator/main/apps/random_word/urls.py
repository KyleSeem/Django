from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^getWord$', views.getWord),
    url(r'^clear$', views.clear)
]
