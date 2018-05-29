from django.shortcuts import render, redirect, HttpResponse
import random, string

def index(request):
    if ('attempt' in request.session) == False:
        request.session['attempt'] = 0
    return render(request, 'random_word/index.html')


def getWord(request):
    if request.method == "POST":
        request.session['randWord'] = ''.join(random.choice(string.digits + string.uppercase) for i in range(14))
        request.session['attempt'] += 1
        return redirect('/')
    else:
        return redirect('/')

def clear(request):
    if request.method == "POST":
        request.session.clear()
        return redirect('/')
    else:
        return redirect('/')
