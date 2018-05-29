from django.conf.urls import url
from . import views

app_name = 'disappearing_ninjas'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ninjas$', views.ninjas, name='all'),
    url(r'^ninjas/(?P<color>\w+)$', views.color, name='ninja_color'),
]
