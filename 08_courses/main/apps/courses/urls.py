from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addCourse$', views.addCourse),
    url(r'^deleteCourse/(?P<id>\d+)$', views.deleteCourse),
    url(r'^comment/(?P<id>\d+)$', views.comment),
]
