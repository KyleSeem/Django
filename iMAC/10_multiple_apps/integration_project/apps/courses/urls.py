from django.conf.urls import url
from . import views

app_name = 'courses'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addCourse$', views.addCourse, name='add'),
    url(r'^deleteCourse/(?P<id>\d+)$', views.deleteCourse, name='delete'),
    url(r'^comments/(?P<id>\d+)$', views.comments, name='comments'),
    url(r'^manager$', views.manager, name='manager'),
    url(r'^register$', views.register, name='register'),
]
