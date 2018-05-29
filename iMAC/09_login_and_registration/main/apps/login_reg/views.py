from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    print (User.objects.all())
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
            return redirect('/')
        elif verify[0] == True:
            request.session['success'] = verify[1]
            return redirect('/success')
        else:
            request.session.clear()
            return redirect('/')


def register(request):
    if request.method == "POST":

        verify = User.userManager.register(request.POST)

        if verify[0] == False:
            for alert in verify[1]:
                messages.add_message(request, messages.INFO, alert)
            return redirect('/')

        elif verify[0] == True:
            request.session['success'] = verify[1]
            return redirect('/success')
        else:
            request.session.clear()
            return redirect('/')



def success(request):
    context = {
        'users':User.objects.all()
    }
    return render(request, 'login_reg/success.html', context)
