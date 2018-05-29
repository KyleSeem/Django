from django.conf.urls import url
from . import views

app_name = 'book_reviews'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
