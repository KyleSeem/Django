from __future__ import unicode_literals

from django.db import models
from ..login_reg.models import User

# Create your models here.
class BookManager(models.Manager):
    def create(self, postData):
        title = postData['title']
        alerts = []

        # try:
        #     book = Book.objects.get(title=title)
        # except:
        #     print ('BOOK ALREADY IN DATABASE')
        #     return (False, 'exists')
        #     # print (book.id)
        #     # return (False, 'exists', book.id)
        # else:
        if len(title) < 1:
            alerts.append('Book title cannot be left blank.')
        if len(postData['authorAdd']) < 1:
            alerts.append('Author cannot be left blank.')
        if len(postData['review']) < 1:
            alerts.append('Review cannot be left blank.')
        if postData['rating'] == 'blank':
            alerts.append('Rating cannot be left blank.')

        if alerts:
            print ('FAILED VALIDATION')
            return (False, alerts)

        else:
            user = User.objects.get(id=int(postData['userID']))
            print(user.id, user.first_name)
            book = Book.objects.create(title=postData['title'], author=postData['authorAdd'])
            print(book.title, book.author)
            this_review = Review.objects.create(book=book, review=postData['review'], rating=postData['rating'])
            print(this_review.review, this_review.rating)

            Reviewer.objects.create(user=user, book=book, review=this_review)
            return (True, 'success', book.id)

    def additional(self, postData):
        alerts = []
        if len(postData['review']) < 1:
            alerts.append('Review cannot be left blank.')
        if postData['rating'] == 'blank':
            alerts.append('Rating cannot be left blank.')

        if alerts:
            return (False, alerts)

        else:
            user = User.objects.get(id=postData['userID'])
            book = Book.objects.get(id=postData['bookID'])
            this_review = Review.objects.create(book=book, review=postData['review'], rating=postData['rating'])

            Reviewer.objects.create(user=user, book=book, review=this_review)
            return (True, 'success')

class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bookManager = BookManager()
    objects = models.Manager()

class Review(models.Model):
    review = models.TextField(max_length=1000)
    rating = models.PositiveSmallIntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reviewer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=1)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
