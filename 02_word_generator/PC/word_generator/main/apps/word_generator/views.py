from django.shortcuts import render, redirect, HttpResponse
import random, string
# REMINDER: this is the CONTROLLER in MVC

def index(request):
    if ('attempt' in request.session) == False:
        request.session['attempt'] = 1
    return render(request, 'word_generator/index.html')

def generate(request):
    if request.method == "POST":
        request.session['random_word'] = ''.join(random.choice(string.digits + string.uppercase) for i in range(14))

        request.session['attempt'] += 1
        print (request.session['attempt'])
        return redirect('/')
    else:
        return redirect('/')
