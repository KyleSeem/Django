from django.conf.urls import url
from . import views

app_name = 'ninja_gold'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process/(?P<location>\w+)$', views.process, name='process'),
    url(r'^reset$', views.reset, name='reset'),
]
