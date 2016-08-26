from django.shortcuts import render, HttpResponse, redirect
import random, string

def index(request):
    if('attempt' in request.session) == False:
        request.session['attempt'] = 1
    return render(request, "word_generator/index.html")

def get_word(request):
    print (request.method)
    if request.method == "POST":
        request.session['rand_word'] = ''.join(random.choice(string.digits + string.uppercase) for i in range(14))

        request.session['attempt'] += 1
        # print (request.session['attempt'])
        return redirect('/')
    else:
        return redirect('/')
