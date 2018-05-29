# login_reg
from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    context = {
        'users':User.objects.all()
    }
    return render(request, 'login_reg/index.html', context)


def login(request):
    if request.method == "POST":
        verify = User.userManager.login(request.POST)

        if verify[0] == False:
            for alert in verify[1]:
                messages.add_message(request, messages.INFO, alert)
            return redirect(reverse('login_reg:index'))

        elif verify[0] == True:
            request.session['success'] = verify[1]
            id = verify[2]
            request.session['userID'] = id
            return redirect(reverse('book_reviews:index', kwargs={'id':id}))

        else:
            request.session.clear()
            return redirect(reverse('login_reg:index'))


def register(request):
    if request.method == "POST":
        verify = User.userManager.register(request.POST)

        if verify[0] == False:
            for alert in verify[1]:
                messages.add_message(request, messages.INFO, alert)
            return redirect(reverse('login_reg:index'))

        elif verify[0] == True:
            request.session['success'] = verify[1]
            id = verify[2]
            return redirect(reverse('book_reviews:index', kwargs={'id':id}))
        else:
            request.session.clear()
            return redirect(reverse('login_reg:index'))


# def success(request, id):
#     context = {
#         'user':User.objects.get(id=id),
#     }
#     return render(request, 'book_reviews/index.html', context)


def logout(request):
    request.session.clear()
    return redirect(reverse('login_reg:index'))


def delete(request, id):
    alerts = []
    if request.method == "POST":
        user = User.objects.get(id=id)
        alerts.append('The account registered under the email address "{}" has been deleted.'.format(user.email))
        user.delete()
        return redirect(reverse('login_reg:index'))
