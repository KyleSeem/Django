from django.conf.urls import url
from . import views

app_name = 'testmodels'
urlpatterns = [
    url(r'^$', views.index)
]
