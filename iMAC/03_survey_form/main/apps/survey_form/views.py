from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    if ('submittal' in request.session) == False:
        request.session['submittal'] = 0
    return render(request, 'survey_form/index.html')


def process(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
        request.session['submittal'] += 1
        return redirect('/results')
    else:
        return redirect('/')

def results(request):
    return render(request, 'survey_form/results.html')
