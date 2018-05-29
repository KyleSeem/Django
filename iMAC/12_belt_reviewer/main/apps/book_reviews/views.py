from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Book, Review, Reviewer, User

# Create your views here.
def index(request, id):
    print(id)
    context = {
        'user':User.objects.get(id=id),
        'books':Book.objects.all(),
        'reviews':Review.objects.all(),
        'reviewers':Reviewer.objects.all()
    }
    return render(request, 'book_reviews/index.html', context)

def add(request):
    # Book.objects.all().delete()
    return render(request, 'book_reviews/addBook.html')

def addBook(request):
    if request.method == "POST":
        verify = Book.bookManager.create(request.POST)

        if verify[0] == False:
            if verify[1] == 'exists':
                print ('nope')
                return HttpResponse('book exists')
            else:
                for alert in verify[1]:
                    messages.add_message(request, messages.INFO, alert)
                return redirect(reverse('book_reviews:add'))

        elif verify[0] == True:
            id = verify[2]
            return redirect(reverse('book_reviews:book', kwargs={'id':id}))

def addReview(request, id):
    if request.method == "POST":
        verify = Book.bookManager.additional(request.POST)

        if verify[0] == False:
            for alert in verify[1]:
                messages.add_message(request, messages.INFO, alert)
            return redirect(reverse('book_reviews:book', kwargs={'id':id}))

        elif verify[0] == True:
            return redirect(reverse('book_reviews:book', kwargs={'id':id}))


def book(request, id):
    context = {
        'book':Book.objects.get(id=id),
        'reviews':Review.objects.all(),
        'reviewers':Reviewer.objects.all()
    }
    return render(request, 'book_reviews/book.html', context)

def delete(request, id):
    if request.method == "GET":
        this_review = Review.objects.get(id=id)
        # delete = Review.objects.get(id=id)
        bookID = this_review.book.id
        print(bookID)
        print ('review id:', id)

        return HttpResponse('delete review function')
