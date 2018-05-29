from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    request.session.flush()
    context = {
        'users':User.objects.all()
    }
    return render(request, 'login_registration/index.html', context)

def process(request, process_type):
    if request.method == "POST":
        # registration process
        if process_type == "register":
            # hold name and email info in session in case of alerts
            request.session['reg_first'] = request.POST['first_name']
            request.session['reg_last'] = request.POST['last_name']
            request.session['reg_email'] = request.POST['email']
        # run registration process
            verify = User.userManager.register(request.POST)
            if verify[0] == False:  # if validation fails, do this:
                for alert in verify[1]:
                    messages.add_message(request, messages.INFO, alert)
                return redirect('/')

            elif verify[0] == True:
                request.session.clear()
                request.session['user_name'] = request.POST['first_name'],
                request.session['salutation'] = 'aboard'

                for alert in verify[1]:
                    messages.add_message(request, messages.INFO, alert)
                return redirect('/success')
        # login process
        elif process_type == "login":
            request.session['email'] = request.POST['email']

            verify = User.userManager.login(request.POST)
            if verify[0] == False:
                for alert in verify[1]:
                    messages.add_message(request, messages.INFO, alert)
                    print ('VALIDATION FAILED')
                    print (alert)
                    return redirect('/')

            elif verify[0] == True:
                request.session['user_name'] = verify[2]
                request.session['salutation'] = 'back'

                return redirect('/success')

def success(request):
    context = {
        'user_name':request.session['user_name'],
        'salutation':request.session['salutation']
    }
    return render(request, 'login_registration/success.html', context)

def delete(request, id):
    alerts = []
    if request.method == "POST":
        user = User.objects.get(id=id)
        alerts.append('The account registered under the email address "{}" has been successfully deleted.'.format(user.email))
        user.delete()
        return redirect('/')
    else:
        return redirect('/success')
