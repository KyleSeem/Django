from django.conf.urls import url
from . import views

app_name = 'random_word'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getWord$', views.getWord, name='getWord'),
    url(r'^clear$', views.clear, name='clear')
]
