from django.shortcuts import render, redirect, HttpResponse
from .models import Email

# Create your views here.
def index(request):
    return render(request, 'email_validation/index.html')

def register(request):
    if request.method == "POST":
        verify = Email.emailManager.validate(request.POST['email'])
        if verify[0] == False:
            request.session['alert'] = verify[1]
            return redirect('/')
        elif verify[0] == True:
            Email.objects.create(email=request.POST['email'])
            request.session['approve'] = verify[1]
            return redirect('/success')
        else:
            request.session.clear()
            return redirect('/')

def success(request):
    if request.method == "GET":
        context = {
            'emails':Email.objects.all()
        }
        return render(request, 'email_validation/success.html', context)
    elif request.method == "POST":
        request.session.clear()
        return redirect('/')

def delete(request, id):
    if request.method == "POST":
        email = Email.objects.get(id=id)
        request.session['approve'] = 'The email address "{}" has been deleted.'.format(email.email)
        email.delete()
        return redirect('/success')
    else:
        return redirect('/success')
