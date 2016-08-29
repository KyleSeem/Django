from django.shortcuts import render, HttpResponse, redirect

def index(request):
    # checks to see if form has already been submitted in current session
    if('submittal' in request.session) == False:
        request.session['submittal'] = 0
    return render(request, 'survey_form/index.html')


def process(request):
    # collects user input and stores in session
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
        # increases form submittal count by 1
        request.session['submittal'] += 1
        return redirect('/results')
    else:
        return redirect('/')

def results(request):
    # updates alert based on times form has been submitted
    if request.session['submittal'] < 2:
        request.session['times'] = 'time'
    else:
        request.session['times'] = 'times'
    return render(request, 'survey_form/results.html')

def reset(request):
    # clears form and session
    request.session.clear()
    return redirect('/')
