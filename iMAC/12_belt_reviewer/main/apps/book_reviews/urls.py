from django.conf.urls import url
from . import views

app_name = 'book_reviews'
urlpatterns = [
    url(r'^books/user(?P<id>\d+)$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^addBook$', views.addBook, name='addBook'),
    url(r'^book/(?P<id>\d+)$', views.book, name='book'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^addReview/(?P<id>\d+)$', views.addReview, name='addReview'),
]
